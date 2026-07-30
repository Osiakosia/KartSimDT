from __future__ import annotations

import bpy

from ..project import setup_project_path


class BuildEngineeringSceneOperator(
    bpy.types.Operator,
):
    """
    Build KartSimDT engineering scene.
    """

    bl_idname = "kartsimdt.build_engineering_scene"
    bl_label = "Build Engineering Scene"

    def execute(
        self,
        context,
    ):
        setup_project_path()

        from blender.builders.build_engineering_scene import (
            build_engineering_scene,
        )

        build_engineering_scene()

        return {"FINISHED"}


def register() -> None:
    bpy.utils.register_class(BuildEngineeringSceneOperator)


def unregister() -> None:
    bpy.utils.unregister_class(BuildEngineeringSceneOperator)
