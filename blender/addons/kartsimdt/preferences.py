from __future__ import annotations

import bpy


class KartSimDTPreferences(
    bpy.types.AddonPreferences,
):
    bl_idname = __package__

    project_root: bpy.props.StringProperty(
        name="Project Root",
        subtype="DIR_PATH",
    )

    def draw(
        self,
        context,
    ):
        layout = self.layout

        layout.label(
            text="KartSimDT Project",
        )

        layout.prop(
            self,
            "project_root",
        )
