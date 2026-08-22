"""
KartSimDT Engineering Scene Builder.

Builds the complete Blender engineering scene for one track.

Architecture
------------
TrackContext
    ↓
EngineeringSceneBuilder
    ├── cleanup
    ├── orthophoto
    ├── track survey
    ├── track design
    ├── track road
    └── viewport

The builder owns scene orchestration.
Individual generators own individual visualization objects.
"""

from __future__ import annotations

import bpy

from blender.cleanup import cleanup_scene
from blender.importers.import_orthophoto import import_orthophoto
from blender.importers.import_track_survey import import_track_survey
from blender.viewport import reset_viewport
from kartsimdt.track.context import TrackContext
from kartsimdt.track.design import TrackDesign
from kartsimdt.visualization.blender.generators.start_finish_generator import (
    StartFinishGenerator,
)
from kartsimdt.visualization.blender.generators.track_road_generator import (
    TrackRoadGenerator,
)


class EngineeringSceneBuilder:
    """Build the Blender engineering scene for one track."""

    def __init__(
        self,
        track_context: TrackContext,
    ) -> None:
        self._track_context = track_context

    @property
    def track_context(self) -> TrackContext:
        """Return the active track context."""
        return self._track_context

    def build(self) -> dict[str, bpy.types.Object]:
        """
        Build the complete engineering scene.

        Returns
        -------
        dict[str, bpy.types.Object]
            Generated Blender scene objects.
        """

        print("=" * 60)
        print("KartSimDT Engineering Scene Builder")
        print("=" * 60)

        print()
        print("Active Track")
        print(f"Track      : {self._track_context.name}")
        print(f"Track Root : {self._track_context.root}")

        # ------------------------------------------------------
        # 1. CLEANUP
        # ------------------------------------------------------

        print()
        print("Cleaning Blender scene...")

        cleanup_scene()

        # ------------------------------------------------------
        # 2. ORTHOPHOTO
        # ------------------------------------------------------

        print()
        print("Importing orthophoto...")

        orthophoto = import_orthophoto()

        print(
            f"Orthophoto imported: {orthophoto.name}",
        )

        # ------------------------------------------------------
        # 3. TRACK SURVEY
        # ------------------------------------------------------

        print()
        print("Importing track survey...")

        track_survey = import_track_survey(
            self._track_context,
        )

        print(
            f"Track survey imported: {track_survey.name}",
        )

        # ------------------------------------------------------
        # 4. TRACK DESIGN
        # ------------------------------------------------------

        print()
        print("Loading track design...")

        design = TrackDesign.from_context(
            self._track_context,
        )

        print("Track design loaded.")

        # ------------------------------------------------------
        # 5. TRACK ROAD
        # ------------------------------------------------------

        print()
        print("Generating TrackRoad...")

        track_road = TrackRoadGenerator(
            design,
        ).generate_from_object(
            track_survey,
        )

        print(
            f"Track road generated: {track_road.name}",
        )

        # ------------------------------------------------------
        # 6. START / FINISH
        # ------------------------------------------------------

        print()
        print("Generating Start/Finish...")

        start_finish = StartFinishGenerator(
            self._track_context,
        ).generate()

        # ------------------------------------------------------
        # 7. VIEWPORT
        # ------------------------------------------------------

        print()
        print("Resetting viewport...")

        reset_viewport()

        # ------------------------------------------------------
        # 8. RESULT
        # ------------------------------------------------------

        objects: dict[str, bpy.types.Object] = {
            "orthophoto": orthophoto,
            "track_survey": track_survey,
            "track_road": track_road,
        }

        if start_finish is not None:
            objects["start_finish"] = start_finish

        print()
        print("Engineering scene ready.")

        print("=" * 60)

        return objects
