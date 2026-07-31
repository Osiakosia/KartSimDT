"""
KartSimDT Calibration Panel

Responsibilities
----------------
- Draw the Calibration section.
- Display Orthophoto calibration controls.
- Display calibration operators.

Does NOT
---------
- Apply transforms.
- Modify Blender objects.
- Read or write calibration files.
"""

from __future__ import annotations

import bpy


def draw_calibration(
    layout: bpy.types.UILayout,
    context: bpy.types.Context,
) -> None:
    """
    Draw the Calibration section.
    """
    print("DRAW CALIBRATION")

    props = context.scene.kartsimdt_calibration
    print(props)

    props = context.scene.kartsimdt_calibration

    box = layout.box()

    box.label(
        text="Calibration",
        icon="EMPTY_AXIS",
    )

    #
    # Orthophoto
    #

    col = box.column(align=True)

    col.label(
        text="Orthophoto",
        icon="IMAGE_DATA",
    )

    #
    # Calibration Properties
    #

    print("Drawing properties...")
    col.prop(props, "orthophoto_scale")
    col.prop(props, "orthophoto_rotation")
    col.prop(props, "orthophoto_offset_x")
    col.prop(props, "orthophoto_offset_y")

    col.separator()

    col.prop(props, "live_update")

    #
    # Operators
    #

    row = box.row(align=True)

    row.operator(
        "kartsimdt.save_calibration",
        text="Save",
        icon="FILE_TICK",
    )

    row.operator(
        "kartsimdt.reset_calibration",
        text="Reset",
        icon="LOOP_BACK",
    )
