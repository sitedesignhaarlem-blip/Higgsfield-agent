#!/usr/bin/env python3
"""
assemble.py — plakt genormaliseerde clips aan elkaar met crossfades.

Gebruik:
    python3 assemble.py clips/norm output/Southern_Cross.mp4 --xfade 0.4

Verwacht dat alle clips in de inputmap:
  - dezelfde resolutie, fps en SAR hebben (normaliseer eerst!)
  - alfabetisch/numeriek op volgorde staan (01_, 02_, 03_, ...)

Normaliseren doe je vooraf met:
    ffmpeg -i raw.mp4 \
      -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1" \
      -r 30 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -an norm.mp4
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm"}


def probe_duration(path: Path) -> float:
    """Exacte duur van een clip via ffprobe."""
    out = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "json", str(path),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(json.loads(out.stdout)["format"]["duration"])


def build_filter(durations, xfade, transition="fade"):
    """
    Bouwt de xfade-keten.

    Offset van overgang k (0-based) = som(d[0..k]) - (k+1) * xfade
    Elke crossfade 'eet' xfade seconden van de totale lengte.
    """
    if len(durations) == 1:
        return None, "[0:v]"

    parts = []
    acc = 0.0
    prev = "[0:v]"

    for i in range(len(durations) - 1):
        acc += durations[i]
        offset = acc - (i + 1) * xfade
        if offset <= 0:
            sys.exit(
                f"Clip {i+1} is te kort ({durations[i]:.2f}s) voor een crossfade "
                f"van {xfade}s. Verlaag --xfade of gebruik langere clips."
            )
        label = f"[v{i+1}]"
        parts.append(
            f"{prev}[{i+1}:v]xfade=transition={transition}:"
            f"duration={xfade}:offset={offset:.3f}{label}"
        )
        prev = label

    return ";".join(parts), prev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indir", help="map met genormaliseerde clips")
    ap.add_argument("output", help="pad naar de eindvideo")
    ap.add_argument("--xfade", type=float, default=0.4,
                    help="crossfade in seconden (default 0.4)")
    ap.add_argument("--transition", default="fade",
                    help="xfade transitietype (default 'fade')")
    ap.add_argument("--crf", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true",
                    help="toon het commando en de lengteberekening, voer niets uit")
    args = ap.parse_args()

    indir = Path(args.indir)
    clips = sorted(p for p in indir.iterdir() if p.suffix.lower() in VIDEO_EXT)

    if not clips:
        sys.exit(f"Geen clips gevonden in {indir}")

    durations = [probe_duration(c) for c in clips]
    total_raw = sum(durations)
    overlap_loss = (len(clips) - 1) * args.xfade
    final_len = total_raw - overlap_loss

    print(f"Clips           : {len(clips)}")
    for c, d in zip(clips, durations):
        print(f"  {c.name:<32} {d:6.2f}s")
    print(f"Ruwe totaallengte : {total_raw:6.2f}s")
    print(f"Crossfade-verlies : {overlap_loss:6.2f}s ({len(clips)-1} x {args.xfade}s)")
    print(f"Eindlengte        : {final_len:6.2f}s")

    if final_len < 60:
        print("\n  LET OP: onder de 60 seconden. Doel is 60-90s.")
    elif final_len > 90:
        print("\n  LET OP: boven de 90 seconden. Doel is 60-90s.")

    filt, last = build_filter(durations, args.xfade, args.transition)

    cmd = ["ffmpeg", "-y"]
    for c in clips:
        cmd += ["-i", str(c)]

    if filt:
        cmd += ["-filter_complex", filt, "-map", last]
    else:
        cmd += ["-map", "0:v"]

    cmd += [
        "-c:v", "libx264",
        "-crf", str(args.crf),
        "-preset", "slow",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-an",
        args.output,
    ]

    if args.dry_run:
        print("\nCommando:\n" + " ".join(cmd))
        return

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True)
    print(f"\nKlaar: {args.output}")


if __name__ == "__main__":
    main()
