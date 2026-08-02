from __future__ import annotations

from pathlib import Path

import bpy
from bpy.app.handlers import persistent


def load_calibration_into_scene() -> None:
    """
    Load saved Orthophoto calibration into Blender UI properties.

    The Orthophoto object itself is transformed by import_orthophoto.py.
    This function only synchronizes the KartSimDT calibration panel.
    """

    scene = bpy.context.scene

    if scene is None:
        return

    if not hasattr(scene, "kartsimdt_calibration"):
        print("KartSimDT calibration properties are not registered.")
        return

    #
    # scene.blend is located next to scene_transform.json.
    #

    blend_file = Path(bpy.data.filepath)

    if not blend_file:
        print("KartSimDT: blend file is not saved.")
        return

    transform_file = blend_file.parent / "scene_transform.json"

    if not transform_file.exists():
        print(
            "KartSimDT: scene_transform.json not found:",
            transform_file,
        )
        return

    #
    # Load directly from this scene's transform file.
    #

    import json

    with transform_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    orthophoto = data["orthophoto"]

    props = scene.kartsimdt_calibration

    #
    # Synchronize UI.
    #

    props.orthophoto_scale = orthophoto["scale"]
    props.orthophoto_rotation = orthophoto["rotation"]
    props.orthophoto_offset_x = orthophoto["offset_x"]
    props.orthophoto_offset_y = orthophoto["offset_y"]

    print()
    print("=" * 60)
    print("KARTSIMDT CALIBRATION UI LOADED")
    print("=" * 60)
    print(f"Transform file : {transform_file}")
    print(f"Scale          : {props.orthophoto_scale}")
    print(f"Rotation       : {props.orthophoto_rotation}")
    print(f"Offset X       : {props.orthophoto_offset_x}")
    print(f"Offset Y       : {props.orthophoto_offset_y}")
    print("=" * 60)


@persistent
def on_load_post(_dummy) -> None:
    """
    Synchronize calibration UI after loading a .blend file.
    """

    load_calibration_into_scene()


def register() -> None:
    """
    Register calibration load handler.
    """
    if on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(on_load_post)


def unregister() -> None:
    """
    Unregister calibration load handler.
    """
    if on_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(on_load_post)
