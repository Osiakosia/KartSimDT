from __future__ import annotations

import bpy


class ResetCalibrationOperator(bpy.types.Operator):
    """
    Reset calibration.
    """

    bl_idname = "kartsimdt.reset_calibration"
    bl_label = "Reset Calibration"

    def execute(self, context):
        return {"FINISHED"}


def register() -> None:
    bpy.utils.register_class(ResetCalibrationOperator)


def unregister() -> None:
    bpy.utils.unregister_class(ResetCalibrationOperator)
