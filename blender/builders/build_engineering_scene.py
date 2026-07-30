"""
Build KartSimDT engineering scene.
"""

from __future__ import annotations

import sys
from pathlib import Path


# from blender.importers.import_walkthrough import (
#     import_walkthrough,
# )

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from blender.cleanup import cleanup_scene # ruff: noqa: E402
from blender.importers.import_orthophoto import import_orthophoto # ruff: noqa: E402
from blender.importers.import_track_survey import import_track_survey # ruff: noqa: E402
from blender.viewport import reset_viewport # ruff: noqa: E402

def build_engineering_scene() -> None:
    """
    Build KartSimDT engineering scene.
    """

    print("=" * 60)
    print("KartSimDT Engineering Scene")
    print("=" * 60)

    cleanup_scene()

    print("Importing orthophoto...")
    orthophoto = import_orthophoto()

    print("Orthophoto imported.")

    print("Importing track survey...")
    track_survey = import_track_survey()

    print("Track survey imported.")

    reset_viewport()

    print()
    print("Imported Objects")
    print(f"Orthophoto   : {orthophoto.name}")
    print(f"Track Survey : {track_survey.name}")

    print()
    print("Engineering scene ready.")

    # print("Importing walkthrough...")
    # walkthrough = import_walkthrough()
    # print("Walkthrough imported.")
    # print(f"Walkthrough : {walkthrough.name}")


def main() -> None:
    build_engineering_scene()


if __name__ == "__main__":
    main()
