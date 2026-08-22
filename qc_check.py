#!/usr/bin/env python3
"""
qc_check.py — automatische kwaliteitscontrole op gegenereerde clips.

Detecteert drie soorten problemen:
  1. JERK      — schokkende / springende camera, golvende geometrie
  2. EDGE      — rechte lijnen (relingen, kozijnen, rompnaden) die oplossen of flikkeren
  3. DRIFT     — het beeld loopt zo ver weg van de bronfoto dat het model dingen verzint

Daarnaast maakt het per clip een contactsheet zodat je de clip VISUEEL kunt nakijken.
De scores vinden bewegingsproblemen. Verzonnen objecten vind je alleen met je ogen.
Beide stappen zijn verplicht.

Gebruik:
    pip install opencv-python numpy --break-system-packages
    python3 qc_check.py clips/raw --shotlist shotlist.json --out qc/

Output:
    qc/report.json          alle scores
    qc/sheets/<clip>.jpg    contactsheet per clip (12 frames in een raster)
    printed tabel, gesorteerd op verdachtheid
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

try:
    import cv2
    import numpy as np
except ImportError:
    sys.exit("Installeer eerst: pip install opencv-python numpy --break-system-packages")

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm"}

# Drempels. Boven deze waarden gaat een clip naar handmatige inspectie.
JERK_THRESHOLD = 2.5    # 95e percentiel jerk t.o.v. mediane beweging
EDGE_CV_THRESHOLD = 0.22  # variatiecoefficient van de randdichtheid
DRIFT_THRESHOLD = 0.38   # genormaliseerd verschil laatste frame vs. bronfoto

SAMPLE_FPS = 10          # frames per seconde die we analyseren
ANALYSIS_WIDTH = 480     # downscale voor snelheid


def read_frames(path, sample_fps=SAMPLE_FPS, width=ANALYSIS_WIDTH):
    """Leest de clip uit en geeft een lijst grijswaarde-frames terug."""
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise RuntimeError(f"Kan clip niet openen: {path}")

    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    step = max(1, int(round(src_fps / sample_fps)))

    frames, color_frames, idx = [], [], 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            h, w = frame.shape[:2]
            scale = width / float(w)
            small = cv2.resize(frame, (width, max(1, int(h * scale))))
            color_frames.append(small)
            frames.append(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY))
        idx += 1
    cap.release()

    if len(frames) < 4:
        raise RuntimeError(f"Te weinig frames in {path}")
    return frames, color_frames


def jerk_score(frames):
    """
    Optical flow (Farneback) -> gemiddelde bewegingsgrootte per frame
    -> versnelling -> jerk. Hoge pieken = de camera springt of de
    geometrie vervormt schoksgewijs.
    """
    magnitudes = []
    for a, b in zip(frames[:-1], frames[1:]):
        flow = cv2.calcOpticalFlowFarneback(
            a, b, None,
            pyr_scale=0.5, levels=3, winsize=15,
            iterations=3, poly_n=5, poly_sigma=1.2, flags=0,
        )
        mag = np.sqrt(flow[..., 0] ** 2 + flow[..., 1] ** 2)
        magnitudes.append(float(np.mean(mag)))

    mags = np.array(magnitudes)
    if len(mags) < 3:
        return 0.0, mags.tolist()

    accel = np.diff(mags)
    jerk = np.abs(np.diff(accel))

    baseline = float(np.median(mags))
    if baseline < 1e-6:
        baseline = 1e-6

    score = float(np.percentile(jerk, 95) / baseline)
    return score, mags.tolist()


def edge_stability(frames):
    """
    Randdichtheid per frame via Canny. Rechte lijnen op een jacht
    (relingen, kozijnen, rompnaden) horen stabiel te blijven. Een hoge
    variatiecoefficient betekent dat structuur oplost of flikkert.
    """
    densities = []
    for f in frames:
        edges = cv2.Canny(f, 80, 180)
        densities.append(float(np.count_nonzero(edges)) / edges.size)

    d = np.array(densities)
    mean = float(np.mean(d))
    if mean < 1e-6:
        return 0.0, densities
    return float(np.std(d) / mean), densities


def drift_score(color_frames, reference_path):
    """
    Vergelijkt het laatste frame met de bronfoto. Een groot verschil
    betekent dat het model ver van het origineel is afgedwaald - de
    belangrijkste voorbode van verzonnen objecten.
    """
    ref = cv2.imread(str(reference_path))
    if ref is None:
        return None

    last = color_frames[-1]
    h, w = last.shape[:2]
    ref = cv2.resize(ref, (w, h))

    a = cv2.cvtColor(last, cv2.COLOR_BGR2GRAY).astype(np.float32)
    b = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY).astype(np.float32)

    a = cv2.GaussianBlur(a, (5, 5), 0)
    b = cv2.GaussianBlur(b, (5, 5), 0)

    diff = np.abs(a - b) / 255.0
    return float(np.mean(diff) * 3.0)  # geschaald naar een leesbaar bereik


def contact_sheet(clip, out_path, tiles=(4, 3)):
    """12 frames in een raster, zodat je de clip in een oogopslag kunt scannen."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cols, rows = tiles
    n = cols * rows

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(clip)],
        capture_output=True, text=True, check=True,
    )
    dur = float(json.loads(probe.stdout)["format"]["duration"])

    fps = n / max(dur, 0.1)

    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", str(clip),
         "-vf", f"fps={fps:.4f},scale=480:-1,tile={cols}x{rows}",
         "-frames:v", "1", "-q:v", "3", str(out_path)],
        check=True,
    )


def load_reference_map(shotlist_path, indir):
    """Koppelt clipnummer aan de bronfoto uit de shotlist."""
    if not shotlist_path:
        return {}
    data = json.loads(Path(shotlist_path).read_text())
    refs = {}
    for clip in data.get("clips", []):
        ref = clip.get("end_image") or clip.get("start_image")
        if ref:
            refs[int(clip["index"])] = Path(ref)
    return refs


def clip_index(path):
    """Haalt het clipnummer uit een bestandsnaam als 01_exterior.mp4."""
    stem = path.stem.split("_")[0]
    return int(stem) if stem.isdigit() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indir", help="map met clips")
    ap.add_argument("--shotlist", default=None, help="shotlist.json voor drift-check")
    ap.add_argument("--out", default="qc", help="outputmap")
    ap.add_argument("--no-sheets", action="store_true", help="sla contactsheets over")
    args = ap.parse_args()

    indir = Path(args.indir)
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    clips = sorted(p for p in indir.iterdir() if p.suffix.lower() in VIDEO_EXT)
    if not clips:
        sys.exit(f"Geen clips gevonden in {indir}")

    refs = load_reference_map(args.shotlist, indir)
    results = []

    for clip in clips:
        try:
            frames, color = read_frames(clip)
            jerk, mags = jerk_score(frames)
            edge_cv, densities = edge_stability(frames)

            drift = None
            idx = clip_index(clip)
            if idx is not None and idx in refs and refs[idx].exists():
                drift = drift_score(color, refs[idx])

            sheet = None
            if not args.no_sheets:
                sheet = outdir / "sheets" / f"{clip.stem}.jpg"
                contact_sheet(clip, sheet)

            flags = []
            if jerk > JERK_THRESHOLD:
                flags.append("JERK")
            if edge_cv > EDGE_CV_THRESHOLD:
                flags.append("EDGE")
            if drift is not None and drift > DRIFT_THRESHOLD:
                flags.append("DRIFT")

            results.append({
                "clip": clip.name,
                "index": idx,
                "jerk": round(jerk, 3),
                "edge_cv": round(edge_cv, 3),
                "drift": round(drift, 3) if drift is not None else None,
                "flags": flags,
                "sheet": str(sheet) if sheet else None,
                "motion_profile": [round(m, 4) for m in mags],
                "edge_profile": [round(d, 5) for d in densities],
            })

        except Exception as exc:
            results.append({
                "clip": clip.name,
                "index": clip_index(clip),
                "error": str(exc),
                "flags": ["ERROR"],
            })

    results.sort(key=lambda r: (-len(r.get("flags", [])), -(r.get("jerk") or 0)))

    (outdir / "report.json").write_text(json.dumps(results, indent=2))

    print(f"{'CLIP':<30} {'JERK':>7} {'EDGE':>7} {'DRIFT':>7}  FLAGS")
    print("-" * 70)
    for r in results:
        if "error" in r:
            print(f"{r['clip']:<30} {'-':>7} {'-':>7} {'-':>7}  ERROR: {r['error']}")
            continue
        drift = f"{r['drift']:.3f}" if r["drift"] is not None else "-"
        print(f"{r['clip']:<30} {r['jerk']:>7.2f} {r['edge_cv']:>7.3f} {drift:>7}  "
              f"{','.join(r['flags']) if r['flags'] else 'ok'}")

    flagged = [r for r in results if r.get("flags")]
    print("-" * 70)
    print(f"{len(flagged)} van {len(results)} clips gemarkeerd voor inspectie.")
    print(f"\nRapport: {outdir/'report.json'}")
    if not args.no_sheets:
        print(f"Contactsheets: {outdir/'sheets'}")
    print("\nVERPLICHT: bekijk ALLE contactsheets, niet alleen de gemarkeerde.")
    print("Verzonnen objecten geven geen hoge score - die zie je alleen met je ogen.")


if __name__ == "__main__":
    main()
