"""Entrypoint: copy the entry image into the grader's output directory.

Standard library only. Reads entry.png from this file's own directory and
writes the same bytes to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png
when the variable is unset). The copy is byte for byte, so repeated runs
always produce identical output.
"""

import os
import sys
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    with open(source, "rb") as handle:
        data = handle.read()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    with open(target, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
