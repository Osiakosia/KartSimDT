"""
Import Walkthrough centerline into Blender.
"""

from __future__ import annotations

import json
from pathlib import Path

import bpy

from blender.importers.import_track_survey import (
    apply_track_centerline_transform,
    create_track_survey_curve,
    extract_points,
    load_track_survey,
)


def import_walkthrough() -> bpy.types.Object:
    """
    Import Walkthrough centerline JSON.
    """

    root = Path(__file__).resolve().parents[2]

    track_folder = root / "data" / "tracks" / "Aukštadvaris"

    input_file = track_folder / "walkthrough" / "centerline.json"

    transform_file = track_folder / "blender" / "scene_transform.json"

    data = load_track_survey(
        input_file,
    )

    with transform_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        transform = json.load(file)

    points = extract_points(
        data,
    )

    from math import sqrt

    print()
    print("Distance diagnostics")
    print("-" * 60)

    max_distance = 0.0
    max_index = 0

    for i in range(1, len(points)):
        dx = points[i][0] - points[i - 1][0]
        dy = points[i][1] - points[i - 1][1]
        dz = points[i][2] - points[i - 1][2]

        distance = sqrt(dx * dx + dy * dy + dz * dz)

        if distance > max_distance:
            max_distance = distance
            max_index = i

    print(f"Maximum step : {max_distance:.3f} m")
    print(f"Between      : {max_index - 1} -> {max_index}")
    print(f"Point A      : {points[max_index - 1]}")
    print(f"Point B      : {points[max_index]}")
    print()

    print()
    print("=" * 60)
    print("Walkthrough Blender Import")
    print("=" * 60)
    print()

    print(f"Format       : {data['format']}")
    print(f"Version      : {data['version']}")
    print(f"Geometry     : {data['geometry']}")
    print(f"Coordinate   : {data['coordinate_system']}")
    print(f"Name         : {data['name']}")
    print(f"Points       : {data['point_count']}")
    print(f"Extracted    : {len(points)}")
    print()

    if points:
        print("Point Preview")
        print(f"First        : {points[0]}")
        print(f"Last         : {points[-1]}")
        print()

        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        zs = [p[2] for p in points]

        print("Bounds")
        print(f"X            : {min(xs):.3f} -> {max(xs):.3f}")
        print(f"Y            : {min(ys):.3f} -> {max(ys):.3f}")
        print(f"Z            : {min(zs):.3f} -> {max(zs):.3f}")
        print()

    curve = create_track_survey_curve(
        "Walkthrough",
        points,
    )

    curve["source_file"] = data["name"]

    apply_track_centerline_transform(
        curve,
        transform["track_centerline"],
    )

    bpy.context.scene.collection.objects.link(
        curve,
    )

    print("Curve Created")
    print(f"Object Name  : {curve.name}")
    print(f"Object Type  : {curve.type}")
    print(f"Splines      : {len(curve.data.splines)}")

    if curve.data.splines:
        print(f"Curve Points : {len(curve.data.splines[0].points)}")

    print()
    print("Import Preview : PASS")
    print()

    return curve
