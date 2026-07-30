"""
Run Blender reference centerline exporter.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from blender.config import BLENDER_EXE

ROOT = Path(__file__).resolve().parents[2]

BLEND_FILE = ROOT / "data" / "reference_tracks" / "Aukstadvaris.blend"

SCRIPT = ROOT / "blender" / "exporters" / "export_reference_centerline.py"


def main() -> None:
    """
    Run the Blender reference centerline exporter.
    """

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
