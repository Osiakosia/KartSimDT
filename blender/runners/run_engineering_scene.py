"""
Run KartSimDT Engineering Scene in Blender GUI.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from blender.config import BLENDER_EXE

ROOT = Path(__file__).resolve().parents[2]

BLEND_FILE = ROOT / "data" / "tracks" / "Aukštadvaris" / "blender" / "scene.blend"

BLENDER_SCRIPT = ROOT / "blender" / "runners" / "execute_engineering_scene.py"


def main() -> None:
    print("Blender :", BLENDER_EXE)
    print("Project :", ROOT)
    print("Blend   :", BLEND_FILE)
    print("Script  :", BLENDER_SCRIPT)

    if not BLEND_FILE.exists():
        raise FileNotFoundError(f"Blend file not found:\n{BLEND_FILE}")

    if not BLENDER_SCRIPT.exists():
        raise FileNotFoundError(f"Blender runner not found:\n{BLENDER_SCRIPT}")

    subprocess.run(
        [
            str(BLENDER_EXE),
            str(BLEND_FILE),
            "--python",
            str(BLENDER_SCRIPT),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
