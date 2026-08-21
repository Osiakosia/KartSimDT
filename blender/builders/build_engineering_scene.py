"""
Build KartSimDT engineering scene.
"""

# ruff: noqa: E402

from __future__ import annotations

import sys
from pathlib import Path

import bpy

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

VENV_SITE_PACKAGES = ROOT / ".venv" / "Lib" / "site-packages"

if VENV_SITE_PACKAGES.is_dir() and str(VENV_SITE_PACKAGES) not in sys.path:
    sys.path.insert(0, str(VENV_SITE_PACKAGES))


from blender.cleanup import cleanup_scene
from blender.importers.import_orthophoto import import_orthophoto
from blender.importers.import_track_survey import import_track_survey
from blender.viewport import reset_viewport
from kartsimdt.track.design import TrackDesign
from kartsimdt.visualization.blender.generators.track_road_generator import (
    TrackRoadGenerator,
)


def print_scene_objects(
    title: str,
) -> None:
    """Print current Blender scene objects."""

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    for obj in bpy.context.scene.objects:
        print(f"{obj.name:25} " f"{obj.type:8} " f"library={obj.library}")

    print("=" * 60)


def build_engineering_scene(
    track_context,
) -> None:
    """Build the Blender engineering scene."""

    print("=" * 60)
    print("KartSimDT Engineering Scene")
    print("=" * 60)

    # ----------------------------------------------------------
    # 1. CLEANUP
    # ----------------------------------------------------------

    cleanup_scene()

    print_scene_objects(
        "SCENE AFTER CLEANUP",
    )

    # ----------------------------------------------------------
    # 2. TRACK CONTEXT
    # ----------------------------------------------------------

    print()
    print("Active Track")
    print(f"Track         : {track_context.name}")
    print(f"Track Root    : {track_context.root}")

    # ----------------------------------------------------------
    # 3. ORTHOPHOTO
    # ----------------------------------------------------------

    print()
    print("Importing orthophoto...")

    orthophoto = import_orthophoto()

    print("Orthophoto imported.")

    # ----------------------------------------------------------
    # 4. TRACK SURVEY
    # ----------------------------------------------------------

    print()
    print("Importing track survey...")

    track_survey = import_track_survey(
        track_context,
    )
    print()
    print("Loading track design...")

    design = TrackDesign.from_context(
        track_context,
    )

    print("Track design loaded.")

    print()
    print("Generating TrackRoad...")

    track_road = TrackRoadGenerator(
        design,
    ).generate_from_object(
        track_survey,
    )

    print("Track road generated.")

    print("Track survey imported.")

    # ----------------------------------------------------------
    # 5. VIEWPORT
    # ----------------------------------------------------------

    reset_viewport()

    # ----------------------------------------------------------
    # 6. RESULT
    # ----------------------------------------------------------

    print()
    print_scene_objects(
        "ENGINEERING SCENE",
    )

    print()
    print("Imported Objects")
    print(f"Orthophoto   : {orthophoto.name}")
    print(f"Track Survey : {track_survey.name}")
    print(f"Track Road   : {track_road.name}")
    print()
    print("Engineering scene ready.")


def main() -> None:
    """Standalone entry point."""

    raise RuntimeError("build_engineering_scene.main() requires TrackContext.")


if __name__ == "__main__":
    main()
