"""
Build Blender scene. scene,py .
"""

from __future__ import annotations

import bpy

from blender.cleanup import cleanup_scene
from blender.importers.import_orthophoto import import_orthophoto
from blender.importers.import_track_survey import import_track_survey
from blender.viewport import reset_viewport


def debug_scene() -> None:
    """
    Print current Blender scene.
    """

    print()
    print("=" * 60)
    print("SCENE READY")
    print("=" * 60)

    print()

    print("Current Blend")
    print(bpy.data.filepath)

    print()

    print("Active Object")
    print(bpy.context.active_object)

    print()

    print("Scene Objects")

    for obj in sorted(
        bpy.context.scene.objects,
        key=lambda o: o.name,
    ):
        print(f"{obj.name:25}" f"{obj.type:10}")

    print()

    print("Object Details")

    for obj in sorted(
        bpy.context.scene.objects,
        key=lambda o: o.name,
    ):
        print("-" * 60)
        print(f"Name      : {obj.name}")
        print(f"Type      : {obj.type}")
        print(f"Location  : {tuple(obj.location)}")
        print(f"Rotation  : {tuple(obj.rotation_euler)}")
        print(f"Scale     : {tuple(obj.scale)}")

        if obj.type == "MESH":
            print(f"Vertices  : {len(obj.data.vertices)}")

        if obj.type == "CURVE":
            print(f"Splines   : {len(obj.data.splines)}")


def main() -> None:
    """
    Build Blender scene.
    """

    print()
    print("=" * 60)
    print("BUILD SCENE")
    print("=" * 60)

    reset_viewport()

    cleanup_scene()

    orthophoto = import_orthophoto()

    track_survey = import_track_survey()

    print()
    print("=" * 60)
    print("SCENE READY")
    print("=" * 60)

    print()
    print("Scene Objects")

    for obj in sorted(
        bpy.context.scene.objects,
        key=lambda o: o.name,
    ):
        print(f"{obj.name:25} {obj.type}")

    print()
    print("Imported Objects")

    print(f"Orthophoto       : {orthophoto.name}")
    print(f"TrackSurvey : {track_survey.name}")

    print()
    print("Current Blend")

    print(bpy.data.filepath)

    debug_scene()


if __name__ == "__main__":
    main()
