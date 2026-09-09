#!/usr/bin/env python3
"""
qc_check.py — automatische kwaliteitscontrole op gegenereerde clips.

Detecteert vier soorten problemen:
  1. JERK      — schokkende / springende camera, golvende geometrie
  2. EDGE      — rechte lijnen (relingen, kozijnen, rompnaden) die oplossen of flikkeren
  3. DRIFT     — het beeld loopt zo ver weg van de bronfoto dat het model dingen verzint
  4. TEXT      — OCR vindt letters/tekst in beeld (bootnamen, instrumentpanelen, labels).
                 Onze prompts bevatten altijd "no text, no lettering, no logos" — elke
                 door OCR gevonden tekst is dus per definitie een afkeuring, ongeacht hoe
                 overtuigend hij oogt (zie Yachti By Nature / "Aventura", 09-09-2026).

Daarnaast maakt het per clip een contactsheet zodat je de clip VISUEEL kunt nakijken.
De JERK/EDGE/DRIFT-scores vinden bewegingsproblemen; TEXT vangt hallucinaties met tekst.
Verzonnen objecten zónder tekst (extra meubels, dieren, boten) vind je alleen met je ogen.
Alle stappen zijn verplicht — TEXT vervangt de visuele check niet, het is een extra laag.

Gebruik:
    pip install opencv-python numpy pytesseract --break-system-packages
    apt-get install -y tesseract-ocr   # of: sudo apt-get install -y tesseract-ocr
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

try:
    import pytesseract
    _HAS_TESSERACT = True
except ImportError:
    _HAS_TESSERACT = False

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm"}

# Drempels. Boven deze waarden gaat een clip naar handmatige inspectie.
JERK_THRESHOLD = 2.5    # 95e percentiel jerk t.o.v. mediane beweging
EDGE_CV_THRESHOLD = 0.22  # variatiecoefficient van de randdichtheid
DRIFT_THRESHOLD = 0.38   # genormaliseerd verschil laatste frame vs. bronfoto
TEXT_MIN_CONF = 45      # OCR-confidence (0-100) waarboven een treffer telt
TEXT_MIN_CHARS = 2      # minimum aantal alfanumerieke tekens in de treffer

SAMPLE_FPS = 10          # frames per seconde die we analyseren (jerk/edge/drift)
ANALYSIS_WIDTH = 480     # downscale voor snelheid (jerk/edge/drift)

# OCR heeft veel meer resolutie nodig dan de bewegingsanalyse: een bootnaam op de
# romp (zoals "Aventura" op Yachti By Nature) is bij 480px breed volledig onleesbaar
# voor tesseract, ook na 4x upscalen van een crop (geteste confidence < 45 op "or").
# Daarom leest text_hits() de clip apart in, op een eigen (hogere) resolutie en een
# lagere sample-rate — OCR is traag, dus we hoeven niet elk jerk/edge-frame te doen.
TEXT_SAMPLE_FPS = 2      # OCR is traag; dit is ruim genoeg voor 3-5s clips
TEXT_ANALYSIS_WIDTH = 1600  # bijna-native breedte; alleen groter dan de bronclip wordt niet upscaled


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


def text_hits(path, sample_fps=TEXT_SAMPLE_FPS, width=TEXT_ANALYSIS_WIDTH):
    """
    Leest de clip apart in op (bijna-)volle resolutie en draait OCR per
    gesamplet frame. Geeft elke geloofwaardige tekst-treffer terug (tijdstip,
    tekst, confidence). Onze prompts verbieden tekst/letters/logo's altijd
    expliciet — dus elke treffer hier betekent dat Kling die regel heeft
    genegeerd (bootnamen op de romp, onzin-tekst op panelen, etc.).

    Belangrijk: dit moet op hoge resolutie, niet op de 480px-frames die
    jerk/edge/drift gebruiken. Een bootnaam als "Aventura" op de romp
    (Yachti By Nature, 09-09-2026) is bij 480px breed voor tesseract volledig
    onleesbaar (geteste confidence < 45, ook na 4x upscalen van een crop) —
    die hallucinatie is destijds alleen gevonden door de video handmatig
    frame-voor-frame te bekijken. Vandaar de eigen, hogere resolutie hier.
    """
    if not _HAS_TESSERACT:
        return None  # OCR niet beschikbaar; caller slaat de TEXT-check over

    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        return []

    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    step = max(1, int(round(src_fps / sample_fps)))

    hits = []
    seen = set()
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            h, w = frame.shape[:2]
            if w < width:
                scale = width / float(w)
                frame = cv2.resize(frame, (width, max(1, int(h * scale))),
                                    interpolation=cv2.INTER_CUBIC)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            data = pytesseract.image_to_data(rgb, output_type=pytesseract.Output.DICT)
            for text, conf in zip(data["text"], data["conf"]):
                cleaned = text.strip()
                alnum = sum(c.isalnum() for c in cleaned)
                try:
                    conf = float(conf)
                except (TypeError, ValueError):
                    continue
                if conf < TEXT_MIN_CONF or alnum < TEXT_MIN_CHARS:
                    continue
                key = cleaned.lower()
                if key in seen:
                    continue
                seen.add(key)
                hits.append({
                    "t": round(idx / src_fps, 2),
                    "text": cleaned,
                    "conf": round(conf, 1),
                })
        idx += 1
    cap.release()
    return hits


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
            text = text_hits(clip)

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
            if text:
                flags.append("TEXT")

            results.append({
                "clip": clip.name,
                "index": idx,
                "jerk": round(jerk, 3),
                "edge_cv": round(edge_cv, 3),
                "drift": round(drift, 3) if drift is not None else None,
                "text_hits": text if text else [],
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

    if not _HAS_TESSERACT:
        print("WAARSCHUWING: pytesseract/tesseract niet gevonden — TEXT-check is OVERGESLAGEN.")
        print("  Installeer: apt-get install -y tesseract-ocr && pip install pytesseract --break-system-packages")
        print("  Zonder deze check vind je tekst-hallucinaties (bv. bootnamen) alleen nog visueel.\n")

    print(f"{'CLIP':<30} {'JERK':>7} {'EDGE':>7} {'DRIFT':>7}  {'TEXT':>4}  FLAGS")
    print("-" * 78)
    for r in results:
        if "error" in r:
            print(f"{r['clip']:<30} {'-':>7} {'-':>7} {'-':>7}  {'-':>4}  ERROR: {r['error']}")
            continue
        drift = f"{r['drift']:.3f}" if r["drift"] is not None else "-"
        text_n = len(r.get("text_hits") or [])
        text_col = str(text_n) if text_n else ("-" if not _HAS_TESSERACT else "0")
        print(f"{r['clip']:<30} {r['jerk']:>7.2f} {r['edge_cv']:>7.3f} {drift:>7}  {text_col:>4}  "
              f"{','.join(r['flags']) if r['flags'] else 'ok'}")
        for hit in r.get("text_hits") or []:
            print(f"    -> t={hit['t']:.1f}s  \"{hit['text']}\"  (conf {hit['conf']:.0f})")

    flagged = [r for r in results if r.get("flags")]
    print("-" * 78)
    print(f"{len(flagged)} van {len(results)} clips gemarkeerd voor inspectie.")
    print(f"\nRapport: {outdir/'report.json'}")
    if not args.no_sheets:
        print(f"Contactsheets: {outdir/'sheets'}")
    print("\nVERPLICHT: bekijk ALLE contactsheets, niet alleen de gemarkeerde.")
    print("TEXT-treffers zijn altijd een afkeuring (onze prompts verbieden tekst/letters/logo's).")
    print("Verzonnen objecten zonder tekst geven geen hoge score - die zie je alleen met je ogen.")


if __name__ == "__main__":
    main()
