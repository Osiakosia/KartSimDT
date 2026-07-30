"""
Run Blender Orthophoto importer.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from blender.config import BLENDER_EXE

ROOT = Path(__file__).resolve().parents[2]

BLEND_FILE = ROOT / "data" / "tracks" / "Aukštadvaris" / "blender" / "scene.blend"

SCRIPT = ROOT / "blender" / "importers" / "import_track_survey.py"


def main() -> None:

    print(BLEND_FILE)
    print(BLEND_FILE.exists())

    subprocess.run(
        [
            str(BLENDER_EXE),
            str(BLEND_FILE),
            "--background",
            "--python",
            str(SCRIPT),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
