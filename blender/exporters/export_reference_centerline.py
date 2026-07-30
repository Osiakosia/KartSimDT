"""
export_reference_centerline.py

Export Blender reference centerline.
"""

from __future__ import annotations

import bpy


def find_centerline() -> bpy.types.Object:
    """
    Find the reference centerline curve.
    """

    obj = bpy.data.objects.get("TrackCenterline")

    if obj is None:
        raise RuntimeError("TrackCenterline object not found.")

    if obj.type != "CURVE":
        raise RuntimeError("TrackCenterline is not a curve.")

    return obj


def extract_points(
    curve: bpy.types.Object,
) -> list[tuple[float, float, float]]:
    """
    Extract centerline points.
    """

    points: list[tuple[float, float, float]] = []

    for spline in curve.data.splines:

        if spline.type == "POLY":

            for point in spline.points:

                points.append(
                    (
                        point.co.x,
                        point.co.y,
                        point.co.z,
                    )
                )

        elif spline.type == "BEZIER":

            for point in spline.bezier_points:

                points.append(
                    (
                        point.co.x,
                        point.co.y,
                        point.co.z,
                    )
                )

    return points


def main() -> None:
    """
    Export reference centerline.
    """

    curve = find_centerline()

    points = extract_points(curve)

    print("=" * 60)
    print("KartSimDT Blender Export")
    print("=" * 60)

    print()

    print(f"Object : {curve.name}")
    print(f"Type   : {curve.type}")
    print(f"Points : {len(points)}")

    print()

    print("First Point")

    print(points[0])

    print()

    print("Last Point")

    print(points[-1])

    print()

    print("Status : PASS")


if __name__ == "__main__":
    main()
