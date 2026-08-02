from __future__ import annotations

import bpy

from ..services import calibration


class ResetCalibrationOperator(bpy.types.Operator):
    """Reset orthophoto calibration."""

    bl_idname = "kartsimdt.reset_calibration"
    bl_label = "Reset Calibration"

    def execute(self, context):
        props = context.scene.kartsimdt_calibration

        # Atstatome numatytą kalibraciją ir įrašome į JSON
        data = calibration.reset_calibration()

        orthophoto = data["orthophoto"]

        # Atnaujiname UI savybes.
        # update= callback'ai automatiškai atnaujins Blender objektą.
        props.orthophoto_scale = orthophoto["scale"]
        props.orthophoto_rotation = orthophoto["rotation"]
        props.orthophoto_offset_x = orthophoto["offset_x"]
        props.orthophoto_offset_y = orthophoto["offset_y"]

        self.report({"INFO"}, "Calibration reset.")

        return {"FINISHED"}


def register() -> None:
    bpy.utils.register_class(ResetCalibrationOperator)


def unregister() -> None:
    bpy.utils.unregister_class(ResetCalibrationOperator)
