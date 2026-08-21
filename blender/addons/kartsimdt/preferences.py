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

    track_name: bpy.props.StringProperty(
        name="Track",
        default="Aukštadvaris",
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

        layout.prop(
            self,
            "track_name",
        )


def register() -> None:
    bpy.utils.register_class(KartSimDTPreferences)


def unregister() -> None:
    bpy.utils.unregister_class(KartSimDTPreferences)
