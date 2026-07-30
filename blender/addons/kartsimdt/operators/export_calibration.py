from __future__ import annotations

import bpy

from ..project import setup_project_path


class ExportCalibrationOperator(
    bpy.types.Operator,
):
    bl_idname = "kartsimdt.export_calibration"
    bl_label = "Export Calibration"

    def execute(
        self,
        context,
    ):
        setup_project_path()

        from blender.exporters.export_calibration import (
            export_calibration,
        )

        export_calibration()

        return {"FINISHED"}


def register() -> None:
    """
    Register Export Calibration operator.
    """
    bpy.utils.register_class(ExportCalibrationOperator)


def unregister() -> None:
    """
    Unregister Export Calibration operator.
    """
    bpy.utils.unregister_class(ExportCalibrationOperator)
