"""
Measure distance between two Google Earth calibration points in Blender.
"""

from __future__ import annotations

import math

import bpy

POINT_A_NAME = "CalibrationPointA"
POINT_B_NAME = "CalibrationPointB"


def get_or_create_point(
    name: str,
) -> bpy.types.Object:
    """
    Get existing calibration point or create a new one.
    """

    obj = bpy.data.objects.get(name)

    if obj is not None:
        return obj

    obj = bpy.data.objects.new(
        name,
        None,
    )

    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 30.0

    bpy.context.scene.collection.objects.link(obj)

    # Separate the points so they are immediately visible.
    if name == POINT_A_NAME:
        obj.location = (-100.0, 0.0, 10.0)

    elif name == POINT_B_NAME:
        obj.location = (100.0, 0.0, 10.0)

    return obj


def measure_points(
    point_a: bpy.types.Object,
    point_b: bpy.types.Object,
) -> None:
    """
    Measure distance between calibration points.
    """

    ax = point_a.location.x
    ay = point_a.location.y

    bx = point_b.location.x
    by = point_b.location.y

    dx = bx - ax
    dy = by - ay

    distance = math.hypot(
        dx,
        dy,
    )

    bpy.context.scene["calibration_point_a"] = f"{ax:.6f}, {ay:.6f}"

    bpy.context.scene["calibration_point_b"] = f"{bx:.6f}, {by:.6f}"

    bpy.context.scene["calibration_distance"] = distance

    print()
    print("=" * 70)
    print("GOOGLE EARTH CALIBRATION MEASUREMENT")
    print("=" * 70)

    print()
    print("Point A")
    print(f"X : {ax:.6f}")
    print(f"Y : {ay:.6f}")

    print()
    print("Point B")
    print(f"X : {bx:.6f}")
    print(f"Y : {by:.6f}")

    print()
    print("Difference")
    print(f"dX : {dx:.6f}")
    print(f"dY : {dy:.6f}")

    print()
    print(f"Distance : {distance:.6f} Blender Units")
    print("=" * 70)

    bpy.context.window_manager.popup_menu(
        lambda self, context: self.layout.label(
            text=f"Distance: {distance:.6f} Blender Units"
        ),
        title="Google Earth Calibration",
        icon="INFO",
    )


def main() -> None:
    point_a = get_or_create_point(
        POINT_A_NAME,
    )

    point_b = get_or_create_point(
        POINT_B_NAME,
    )

    measure_points(
        point_a,
        point_b,
    )


if __name__ == "__main__":
    main()
