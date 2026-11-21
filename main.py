#!/usr/bin/env python3
"""Entry program — make.fun bounty the-catalogue-photo-of-an-2-20261121-0341.

The bounty asks for one catalogue photograph of an impossible
gadget. Ours is the Square Bubble Wand: a polished chrome wand
with a square frame, photographed on a seamless studio backdrop
while the perfect cube-shaped soap bubbles it blows drift around
it — a product shot for a product physics will not allow.

The photograph ships in this repository as entry.png. This
program's only job is to place it at /output/entry.png, which
keeps the run offline and byte-for-byte deterministic.
"""

from pathlib import Path
import shutil

PHOTO = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def main() -> None:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    with PHOTO.open("rb") as src, TARGET.open("wb") as dst:
        # Copy in blocks so the write stays streaming and simple.
        while block := src.read(65536):
            dst.write(block)


if __name__ == "__main__":
    main()
