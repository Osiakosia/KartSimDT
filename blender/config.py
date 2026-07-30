"""
Blender configuration.
"""

from __future__ import annotations

import sys
from pathlib import Path

BLENDER_EXE = Path(r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe")

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def setup_python_path() -> None:
    """
    Add KartSimDT project root to Python path.
    """

    root = str(PROJECT_ROOT)

    if root not in sys.path:
        sys.path.insert(0, root)
