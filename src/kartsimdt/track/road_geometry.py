"""
Road geometry generation.

Pure geometry layer for generating a road surface from a track
centerline and a road-width resolver.

This module must not depend on Blender.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from kartsimdt.track.road_width import RoadWidthResolver


@dataclass(frozen=True, slots=True)
class Point3D:
    """3D point."""

    x: float
    y: float
    z: float


@dataclass(frozen=True, slots=True)
class RoadMesh:
    """Generated road mesh data."""

    vertices: list[Point3D]
    faces: list[tuple[int, int, int, int]]


class RoadGeometryGenerator:
    """Generate road surface geometry from a centerline."""

    def __init__(
        self,
        centerline: Sequence[Point3D],
        width_resolver: RoadWidthResolver,
    ) -> None:
        if len(centerline) < 3:
            raise ValueError("Centerline must contain at least 3 points.")

        self._centerline = centerline
        self._width_resolver = width_resolver

    def generate(self) -> RoadMesh:
        """Generate a closed road mesh."""

        points = self._centerline
        count = len(points)

        vertices: list[Point3D] = []

        for index, point in enumerate(points):
            previous_point = points[(index - 1) % count]
            next_point = points[(index + 1) % count]

            tangent_x = next_point.x - previous_point.x
            tangent_y = next_point.y - previous_point.y

            tangent_length = (tangent_x**2 + tangent_y**2) ** 0.5

            if tangent_length == 0:
                raise ValueError(f"Invalid centerline tangent at index {index}.")

            normal_x = -tangent_y / tangent_length
            normal_y = tangent_x / tangent_length

            width = self._width_resolver.width_for_index(index)
            half_width = width / 2.0

            left = Point3D(
                point.x + normal_x * half_width,
                point.y + normal_y * half_width,
                point.z,
            )

            right = Point3D(
                point.x - normal_x * half_width,
                point.y - normal_y * half_width,
                point.z,
            )

            vertices.extend((left, right))

        faces: list[tuple[int, int, int, int]] = []

        for index in range(count):
            next_index = (index + 1) % count

            left_current = index * 2
            right_current = index * 2 + 1
            left_next = next_index * 2
            right_next = next_index * 2 + 1

            faces.append(
                (
                    left_current,
                    left_next,
                    right_next,
                    right_current,
                )
            )

        return RoadMesh(
            vertices=vertices,
            faces=faces,
        )
