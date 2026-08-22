"""
KartSimDT Start/Finish Blender generator.

The authoritative Start/Finish placement is stored in:

    data/tracks/<track>/design/start_finish.json

This module creates the Blender visualization from that data.

It does not register Blender handlers and does not participate
in addon lifecycle management.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import bpy
from mathutils import Vector

from kartsimdt.track.context import TrackContext

OBJECT_NAME = "StartFinishLine"
OUTPUT_RELATIVE = Path("design") / "start_finish.json"

ROAD_OBJECT_NAME = "TrackRoad"

LINE_BEVEL_DEPTH = 0.08
LINE_BEVEL_RESOLUTION = 2
LINE_Z_OFFSET = 0.03


class StartFinishGenerator:
    """Generate the Start/Finish visualization for a track."""

    def __init__(
        self,
        track_context: TrackContext,
    ) -> None:
        self._track_context = track_context

    @property
    def placement_file(self) -> Path:
        """Return the authoritative Start/Finish JSON file."""

        return self._track_context.root / OUTPUT_RELATIVE

    def generate(self) -> bpy.types.Object | None:
        """
        Generate Start/Finish from the authoritative JSON file.

        Returns
        -------
        bpy.types.Object | None
            Generated StartFinishLine object, or None when placement
            data is unavailable or invalid.
        """

        placement_file = self.placement_file

        if not placement_file.exists():
            print("KartSimDT Start/Finish: " "placement file not found:")
            print(f"  {placement_file}")
            return None

        try:
            data = self._read_json(
                placement_file,
            )

            point_a, point_b = self._read_points(
                data,
            )

        except (
            OSError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
        ) as exc:
            print("KartSimDT Start/Finish: " "invalid placement data:")
            print(f"  {placement_file}")
            print(f"  {exc}")
            return None

        obj = self._create_line(
            point_a,
            point_b,
        )

        print()
        print("=" * 60)
        print("KARTSIMDT START/FINISH GENERATED")
        print("=" * 60)
        print(f"Placement file : {placement_file}")
        print(f"Point A        : " f"{point_a.x:.3f}, " f"{point_a.y:.3f}")
        print(f"Point B        : " f"{point_b.x:.3f}, " f"{point_b.y:.3f}")
        print(f"Object         : {obj.name}")
        print("=" * 60)

        return obj

    @staticmethod
    def _read_json(
        placement_file: Path,
    ) -> dict[str, Any]:
        """Read the authoritative placement JSON."""

        with placement_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data: Any = json.load(file)

        if not isinstance(data, dict):
            raise ValueError(
                "Start/Finish placement JSON must contain an object.",
            )

        return data

    @staticmethod
    def _read_points(
        data: dict,
    ) -> tuple[Vector, Vector]:
        """Extract Start/Finish endpoints from placement data."""

        placement = data["placement"]

        point_a_data = placement["point_a"]
        point_b_data = placement["point_b"]

        point_a = Vector(
            (
                float(point_a_data["x"]),
                float(point_a_data["y"]),
                0.0,
            )
        )

        point_b = Vector(
            (
                float(point_b_data["x"]),
                float(point_b_data["y"]),
                0.0,
            )
        )

        return point_a, point_b

    @staticmethod
    def _road_z_at_xy(
        point: Vector,
    ) -> float:
        """Return TrackRoad elevation at the specified XY position."""

        road = bpy.data.objects.get(
            ROAD_OBJECT_NAME,
        )

        if road is None:
            return float(point.z)

        inverse = road.matrix_world.inverted()

        origin_world = Vector(
            (
                point.x,
                point.y,
                1000.0,
            )
        )

        direction_world = Vector(
            (
                0.0,
                0.0,
                -1.0,
            )
        )

        origin_local = inverse @ origin_world

        direction_local = (inverse.to_3x3() @ direction_world).normalized()

        hit, location, _normal, _face_index = road.ray_cast(
            origin_local,
            direction_local,
        )

        if not hit:
            return float(point.z)

        world_location = road.matrix_world @ location

        return float(world_location.z)

    @classmethod
    def _create_line(
        cls,
        point_a: Vector,
        point_b: Vector,
    ) -> bpy.types.Object:
        """Create or replace the Blender Start/Finish curve."""

        old = bpy.data.objects.get(
            OBJECT_NAME,
        )

        if old is not None:
            bpy.data.objects.remove(
                old,
                do_unlink=True,
            )

        curve_data = bpy.data.curves.new(
            name=f"{OBJECT_NAME}_Curve",
            type="CURVE",
        )

        curve_data.dimensions = "3D"

        spline = curve_data.splines.new(
            "POLY",
        )

        spline.points.add(1)

        z_a = cls._road_z_at_xy(point_a) + LINE_Z_OFFSET

        z_b = cls._road_z_at_xy(point_b) + LINE_Z_OFFSET

        spline.points[0].co = (
            point_a.x,
            point_a.y,
            z_a,
            1.0,
        )

        spline.points[1].co = (
            point_b.x,
            point_b.y,
            z_b,
            1.0,
        )

        curve_data.bevel_depth = LINE_BEVEL_DEPTH

        curve_data.bevel_resolution = LINE_BEVEL_RESOLUTION

        obj = bpy.data.objects.new(
            OBJECT_NAME,
            curve_data,
        )

        bpy.context.scene.collection.objects.link(
            obj,
        )

        return obj
