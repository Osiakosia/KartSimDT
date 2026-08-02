from __future__ import annotations

from typing import Any

import bpy

from ..services import calibration


class SaveCalibrationOperator(bpy.types.Operator):
    """
    Save orthophoto calibration transform.
    """

    bl_idname = "kartsimdt.save_calibration"
    bl_label = "Save Calibration"

    def execute(self, context: bpy.types.Context) -> set[str]:

        props = context.scene.kartsimdt_calibration

        transform: dict[str, Any] = {
            "scale": props.orthophoto_scale,
            "rotation": props.orthophoto_rotation,
            "offset_x": props.orthophoto_offset_x,
            "offset_y": props.orthophoto_offset_y,
        }

        calibration.set_orthophoto_transform(
            transform,
        )

        self.report(
            {"INFO"},
            "Calibration saved",
        )

        return {"FINISHED"}


def register() -> None:
    bpy.utils.register_class(
        SaveCalibrationOperator,
    )


def unregister() -> None:
    bpy.utils.unregister_class(
        SaveCalibrationOperator,
    )
