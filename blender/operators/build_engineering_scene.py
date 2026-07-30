from __future__ import annotations

import bpy

from blender.builders.build_engineering_scene import (
    build_engineering_scene,
)


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
        build_engineering_scene()

        return {"FINISHED"}
