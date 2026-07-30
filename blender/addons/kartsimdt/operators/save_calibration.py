from __future__ import annotations

import bpy


class SaveCalibrationOperator(bpy.types.Operator):
    """
    Save calibration.
    """

    bl_idname = "kartsimdt.save_calibration"
    bl_label = "Save Calibration"

    def execute(self, context):
        return {"FINISHED"}


def register() -> None:
    bpy.utils.register_class(SaveCalibrationOperator)


def unregister() -> None:
    bpy.utils.unregister_class(SaveCalibrationOperator)
