"""
KartSimDT Blender panel.
"""

from __future__ import annotations

import bpy


class KartSimDTPanel(bpy.types.Panel):
    bl_label = "KartSimDT"
    bl_idname = "KARTSIMDT_PT_panel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "KartSimDT"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Engineering")

        layout.operator(
            "kartsimdt.build_engineering_scene",
            icon="SCENE_DATA",
        )

        layout.separator()

        layout.label(text="Calibration")

        layout.operator(
            "kartsimdt.export_calibration",
            icon="EXPORT",
        )


def register() -> None:
    """
    Register panel.
    """
    bpy.utils.register_class(KartSimDTPanel)


def unregister() -> None:
    """
    Unregister panel.
    """
    bpy.utils.unregister_class(KartSimDTPanel)
