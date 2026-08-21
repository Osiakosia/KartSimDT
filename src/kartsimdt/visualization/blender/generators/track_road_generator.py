"""
Track road generator for Blender.

Connects KartSimDT track geometry with the Blender visualization layer.
"""

from __future__ import annotations

import bpy

from kartsimdt.track.design import TrackDesign
from kartsimdt.track.road_geometry import (
    Point3D,
    RoadGeometryGenerator,
)
from kartsimdt.track.road_width import RoadWidthResolver
from kartsimdt.visualization.blender.road import BlenderRoadWriter


class TrackRoadGenerator:
    """Generate a Blender road from KartSimDT track data."""

    def __init__(
        self,
        design: TrackDesign,
    ) -> None:
        self._design = design

    def generate_from_object(
        self,
        centerline_object: bpy.types.Object,
        name: str = "TrackRoad",
    ) -> bpy.types.Object:
        """Generate a Blender road from an existing TrackSurvey object."""

        spline = centerline_object.data.splines[0]

        points = [
            Point3D(
                x=float((centerline_object.matrix_world @ point.co).x),
                y=float((centerline_object.matrix_world @ point.co).y),
                z=float((centerline_object.matrix_world @ point.co).z),
            )
            for point in spline.points
        ]

        width_resolver = RoadWidthResolver(
            self._design.road,
        )

        geometry_generator = RoadGeometryGenerator(
            centerline=points,
            width_resolver=width_resolver,
        )

        road_mesh = geometry_generator.generate()

        return BlenderRoadWriter().create(
            road_mesh,
            name=name,
        )
