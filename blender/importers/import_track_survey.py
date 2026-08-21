"""
Import TrackSurvey centerline into Blender.
"""

from __future__ import annotations

import json
from math import radians
from pathlib import Path

import bpy


def extract_points(
    data: dict,
) -> list[tuple[float, float, float]]:
    """
    Extract centerline points from JSON.
    """

    return [
        (
            point["x"],
            point["y"],
            point["z"],
        )
        for point in data["points"]
    ]


def load_track_survey(
    input_file: Path,
) -> dict:
    """
    Load TrackSurvey JSON.
    """

    with input_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def create_track_survey_curve(
    name: str,
    points: list[tuple[float, float, float]],
) -> bpy.types.Object:
    """
    Create Blender centerline curve.
    """

    curve_data = bpy.data.curves.new(
        name=name,
        type="CURVE",
    )

    curve_data.dimensions = "3D"

    spline = curve_data.splines.new("POLY")

    spline.points.add(len(points) - 1)

    for spline_point, point in zip(
        spline.points,
        points,
        strict=True,
    ):
        spline_point.co = (
            point[0],
            point[1],
            point[2],
            1.0,
        )

    curve_object = bpy.data.objects.new(
        name,
        curve_data,
    )

    return curve_object


def apply_track_centerline_transform(
    curve: bpy.types.Object,
    transform: dict,
) -> None:
    """
    Apply TrackCenterline transform.
    """
    print()
    print("=== TRACK CENTERLINE TRANSFORM DEBUG ===")
    print(f"transform = {transform}")
    print(f"offset_z  = {transform.get('offset_z')}")
    print(f"before location = {tuple(curve.location)}")

    curve.scale.x *= transform["scale"]
    curve.scale.y *= transform["scale"]
    curve.scale.z *= transform.get("scale", 1.0)

    curve.rotation_euler.z = radians(
        transform["rotation_deg"],
    )

    curve.location.x = transform["offset_x"]
    curve.location.y = transform["offset_y"]

    if "offset_z" in transform:
        curve.location.z = transform["offset_z"]

    print(f"after location = {tuple(curve.location)}")
    print("========================================")
    print()


def import_track_survey(
    track_context,
) -> bpy.types.Object:
    """
    Import TrackSurvey centerline using TrackContext.
    """

    input_file = track_context.centerline_json

    transform_file = track_context.blender_dir / "scene_transform.json"

    with transform_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        transform = json.load(file)

    data = load_track_survey(
        input_file,
    )

    points = extract_points(
        data,
    )

    curve = create_track_survey_curve(
        "TrackSurvey",
        points,
    )

    curve["source_file"] = data["name"]

    bpy.context.scene.collection.objects.link(
        curve,
    )

    apply_track_centerline_transform(
        curve,
        transform["track_centerline"],
    )
    bpy.context.view_layer.update()

    print("=" * 60)
    print("KartSimDT Blender Import")
    print("=" * 60)
    print()

    print(f"Format       : {data['format']}")
    print(f"Version      : {data['version']}")
    print(f"Geometry     : {data['geometry']}")
    print(f"Coordinate   : {data['coordinate_system']}")
    print(f"Name         : {data['name']}")
    print(f"Points       : {data['point_count']}")

    print()

    print("Track Context")
    print(f"Track Name   : {track_context.name}")
    print(f"Track Root   : {track_context.root}")

    print()

    print("Curve Created")
    print(f"Object Name  : {curve.name}")
    print(f"Object Type  : {curve.type}")
    print(f"Splines      : {len(curve.data.splines)}")
    print(f"Curve Points : {len(curve.data.splines[0].points)}")

    print()
    print("Import Preview : PASS")

    return curve


def main() -> None:
    raise RuntimeError("import_track_survey.main() requires TrackContext.")


if __name__ == "__main__":
    main()
