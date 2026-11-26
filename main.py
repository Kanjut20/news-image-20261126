"""make.fun bounty: Sum up 26 November's world news in one image.

Deterministic, no network: copies the bundled entry.png to /output/entry.png.
Run twice and both runs write the same bytes.
"""
import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({DST.stat().st_size} bytes, "
          f"sha256={hashlib.sha256(DST.read_bytes()).hexdigest()[:16]}...)")


if __name__ == "__main__":
    main()
