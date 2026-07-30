"""
Run Blender Orthophoto importer (GUI).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from blender.config import BLENDER_EXE

ROOT = Path(__file__).resolve().parents[2]

BLEND_FILE = ROOT / "data" / "reference_tracks" / "test.blend"

SCRIPT = ROOT / "blender" / "importers" / "import_orthophoto.py"


def main() -> None:
    print(BLENDER_EXE)
    subprocess.run(
        [
            str(BLENDER_EXE),
            str(BLEND_FILE),
            "--python",
            str(SCRIPT),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
