#!/usr/bin/env python3
"""news-image-20261119 entry: copy the bundled front page to the output.

The repository ships one file, entry.jpg -- "THE WORLD IN A DAY",
a front page summing up Thursday 19 November 2026, built around the
day's rare news: Voyager 1 confirmed a light-day from home, a new
quantum state in Osaka, a brain score that sees Alzheimer's 12 years
early, Pew's projection that Islam becomes the world's largest faith
by 2035, a new answer for Earth's missing billion years, Somalia's
accusation against the UAE, a tanker hit by projectiles off
Bulgaria, Deutsche Bank's Epstein-linked deals, strikes in Spain
and France, a first for the House Democrats, India-Japan defence
talks and Duckett's 133 -- with the big headlines only in the
ticker. This program writes it to /output/entry.png, byte for byte,
and refuses to write anything else: the bundled file must match its
recorded size and SHA-256, and the copy is checked again after it
lands, including the JPEG start/end markers, so a damaged or swapped
image can never pass as the entry.

The program is deterministic: it reads no clock, no network and no
randomness, so two runs produce identical bytes.

Provenance: entry.jpg was drawn by draw.py (PIL, crisp real text)
over a four-panel AI-generated illustration; the front page was
researched from 19 November 2026 news wires before drawing.
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.jpg"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUT_DIR / "entry.png"

SIZE = 274957
SHA256 = "ac6cdff5837209f887329120fd383f50dcd6f21c74248067df01251cea2fef90"


def die(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def whole_jpeg(path):
    with open(path, "rb") as f:
        start = f.read(2)
        f.seek(-2, os.SEEK_END)
        end = f.read(2)
    return start == b"\xff\xd8" and end == b"\xff\xd9"


def main():
    if not BUNDLED.is_file():
        return die(f"bundled image missing: {BUNDLED}")
    if BUNDLED.stat().st_size != SIZE:
        return die(
            f"bundled image is {BUNDLED.stat().st_size} bytes, "
            f"expected {SIZE}"
        )
    if digest(BUNDLED) != SHA256:
        return die("bundled image hash mismatch")
    if not whole_jpeg(BUNDLED):
        return die("bundled image is not a whole JPEG")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Guard even when the target does not exist yet: if the output
    # directory ever points at this repository, the copy would destroy
    # the bundled image it reads from.
    if TARGET.resolve() == BUNDLED.resolve():
        return die("output would overwrite the bundled image")

    with open(BUNDLED, "rb") as src, open(TARGET, "wb") as dst:
        while True:
            chunk = src.read(65536)
            if not chunk:
                break
            dst.write(chunk)

    if TARGET.stat().st_size != SIZE or digest(TARGET) != SHA256:
        return die("written output failed verification")
    if not whole_jpeg(TARGET):
        return die("written output is not a whole JPEG")

    print(f"wrote {TARGET} ({SIZE} bytes, sha256 {SHA256})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
