"""
Scene debug utilities.
"""

from __future__ import annotations

import bpy


def debug_scene() -> None:
    """
    Print Blender scene information.
    """

    print()
    print("=" * 60)
    print("ENGINEERING SCENE DEBUG")
    print("=" * 60)

    print()
    print(f"Blend File : {bpy.data.filepath or '<Unsaved>'}")
    print(f"Scene      : {bpy.context.scene.name}")

    print()
    print(f"Object Count : {len(bpy.context.scene.objects)}")

    print()
    print("Scene Objects")
    print("-" * 60)

    for obj in sorted(
        bpy.context.scene.objects,
        key=lambda item: item.name,
    ):
        print(f"{obj.name:30} {obj.type}")

    print()
    print("Object Details")
    print("-" * 60)

    for obj in sorted(
        bpy.context.scene.objects,
        key=lambda item: item.name,
    ):

        print()

        print(f"Name      : {obj.name}")
        print(f"Type      : {obj.type}")

        print(
            f"Location  : ({obj.location.x:.3f}, "
            f"{obj.location.y:.3f}, "
            f"{obj.location.z:.3f})"
        )

        print(
            f"Rotation  : ({obj.rotation_euler.x:.3f}, "
            f"{obj.rotation_euler.y:.3f}, "
            f"{obj.rotation_euler.z:.3f})"
        )

        print(
            f"Scale     : ({obj.scale.x:.3f}, "
            f"{obj.scale.y:.3f}, "
            f"{obj.scale.z:.3f})"
        )

        if obj.type == "MESH":
            print(f"Vertices  : {len(obj.data.vertices)}")
            print(f"Materials : {len(obj.material_slots)}")

        elif obj.type == "CURVE":
            print(f"Splines   : {len(obj.data.splines)}")

    print()
    print("=" * 60)
    print("DEBUG COMPLETE")
    print("=" * 60)
