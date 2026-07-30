"""
KartSimDT Calibration Properties

Responsibilities
----------------
- Store interactive calibration values.
- Expose Blender PropertyGroup properties.
- Provide registration functions.

Does NOT
---------
- Draw UI.
- Modify Blender objects.
- Read or write calibration files.
"""

from __future__ import annotations

import bpy
from bpy.props import (
    BoolProperty,
    FloatProperty,
    PointerProperty,
)

print("IMPORT calibration.py")


def register() -> None:
    print("REGISTER CalibrationProperties")

    bpy.utils.register_class(CalibrationProperties)

    bpy.types.Scene.kartsimdt_calibration = PointerProperty(
        type=CalibrationProperties,
    )


class CalibrationProperties(bpy.types.PropertyGroup):
    """
    Interactive calibration properties.
    """

    orthophoto_scale: FloatProperty(
        name="Scale",
        description="Orthophoto scale factor",
        default=1.0,
        min=0.0001,
        precision=6,
    )

    orthophoto_rotation: FloatProperty(
        name="Rotation",
        description="Orthophoto rotation (degrees)",
        default=0.0,
        subtype="ANGLE",
    )

    orthophoto_offset_x: FloatProperty(
        name="Offset X",
        description="Orthophoto X offset",
        default=0.0,
        precision=3,
    )

    orthophoto_offset_y: FloatProperty(
        name="Offset Y",
        description="Orthophoto Y offset",
        default=0.0,
        precision=3,
    )

    live_update: BoolProperty(
        name="Live Update",
        description="Apply changes immediately",
        default=True,
    )


def unregister() -> None:
    """
    Unregister calibration properties.
    """

    del bpy.types.Scene.kartsimdt_calibration

    bpy.utils.unregister_class(CalibrationProperties)
