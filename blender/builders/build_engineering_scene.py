"""
Blender adapter for KartSimDT engineering scene builder.
"""

# ruff: noqa: E402

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT),
    )

VENV_SITE_PACKAGES = ROOT / ".venv" / "Lib" / "site-packages"

if VENV_SITE_PACKAGES.is_dir() and str(VENV_SITE_PACKAGES) not in sys.path:
    sys.path.insert(
        0,
        str(VENV_SITE_PACKAGES),
    )


from kartsimdt.visualization.blender.scene_builder import (
    EngineeringSceneBuilder,
)


def build_engineering_scene(
    track_context,
) -> None:
    """
    Build the Blender engineering scene.

    This module is a thin Blender-side adapter.
    The actual scene orchestration lives in
    KartSimDT visualization.
    """

    EngineeringSceneBuilder(
        track_context,
    ).build()
