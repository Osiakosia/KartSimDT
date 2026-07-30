from __future__ import annotations

import bpy

from blender.exporters.export_calibration import (
    export_calibration,
)


class ExportCalibrationOperator(
    bpy.types.Operator,
):

    bl_idname = "kartsimdt.export_calibration"
    bl_label = "Export Calibration"

    def execute(
        self,
        context,
    ):
        export_calibration()

        self.report(
            {"INFO"},
            "Calibration exported.",
        )

        return {"FINISHED"}
