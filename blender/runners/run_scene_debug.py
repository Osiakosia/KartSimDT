"""
Run Blender Scene (DEBUG).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from blender.config import BLENDER_EXE

ROOT = Path(__file__).resolve().parents[2]

BLEND_FILE = ROOT / "data" / "reference_tracks" / "test.blend"

SCRIPT = ROOT / "blender" / "scene.py"


def main() -> None:

    print("=" * 60)
    print("RUN SCENE DEBUG")
    print("=" * 60)

    print(f"Blender : {BLENDER_EXE}")
    print(f"Blend   : {BLEND_FILE}")
    print(f"Script  : {SCRIPT}")

    subprocess.run(
        [
            str(BLENDER_EXE),
            str(BLEND_FILE),
            "--python",
            str(SCRIPT),
        ],
        check=True,
    )

    print()
    print("=" * 60)
    print("RUN FINISHED")
    print("=" * 60)


if __name__ == "__main__":
    main()
