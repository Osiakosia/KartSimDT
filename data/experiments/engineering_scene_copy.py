"""
Build KartSimDT engineering scene.
"""

from __future__ import annotations

import sys
from pathlib import Path

from blender.cleanup import cleanup_scene
from blender.debug.scene_debug import debug_scene
from blender.importers.import_orthophoto import import_orthophoto
from blender.importers.import_track_survey import import_track_survey
from blender.viewport import reset_viewport

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def build_engineering_scene() -> None:

    print("BUILD START")

    orthophoto = import_orthophoto()

    print("ORTHOPHOTO DONE")

    # track = import_track_survey()

    print("BUILD END")

    print("=" * 60)
    print("KartSimDT Engineering Scene")
    print("=" * 60)
    print()

    cleanup_scene()

    print(">>> BUILD START")

    print(">>> Import orthophoto")
    orthophoto = import_orthophoto()

    print(">>> Orthophoto imported")

    print(">>> Import track survey")
    track = import_track_survey()
    print(track.name)

    print(">>> Track survey imported")

    print(">>> BUILD FINISHED")

    print("Importing Orthophoto...")
    orthophoto = import_orthophoto()

    print()

    print("Importing Track Survey...")
    track_centerline = import_track_survey()

    print()

    reset_viewport()

    debug_scene()

    print()
    print("Imported Objects")
    print(f"Orthophoto      : {orthophoto.name}")
    print(f"Track Survey    : {track_centerline.name}")

    print()
    print("Scene build complete.")

    def main() -> None:
        build_engineering_scene()

    if __name__ == "__main__":
        main()
