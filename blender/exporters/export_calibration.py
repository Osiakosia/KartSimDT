import json
from math import degrees
from pathlib import Path

import bpy


def get_orthophoto() -> bpy.types.Object:
    """
    Return Orthophoto object.
    """

    return bpy.data.objects["Orthophoto"]


def get_track_centerline() -> bpy.types.Object:
    """
    Return TrackCenterline object.
    """

    return bpy.data.objects["TrackCenterline"]


def export_orthophoto(
    orthophoto: bpy.types.Object,
) -> dict:
    """
    Export orthophoto transform.
    """

    return {
        "scale": orthophoto.scale.x,
        "rotation_deg": degrees(
            orthophoto.rotation_euler.z,
        ),
        "offset_x": orthophoto.location.x,
        "offset_y": orthophoto.location.y,
        "offset_z": orthophoto.location.z,
    }


def export_track_centerline(
    centerline: bpy.types.Object,
) -> dict:
    """
    Export TrackCenterline transform.
    """

    return {
        "scale": centerline.scale.x,
        "rotation_deg": degrees(
            centerline.rotation_euler.z,
        ),
        "offset_x": centerline.location.x,
        "offset_y": centerline.location.y,
        "offset_z": centerline.location.z,
    }


def create_scene_transform(
    orthophoto: dict,
    track_centerline: dict,
) -> dict:
    """
    Create scene transform.
    """

    return {
        "orthophoto": orthophoto,
        "track_centerline": track_centerline,
    }


def save_scene_transform(
    output_file: Path,
    scene_transform: dict,
) -> None:
    """
    Save scene transform.
    """

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            scene_transform,
            file,
            indent=4,
        )


def export_calibration() -> None:
    """
    Export scene transform.
    """

    root = Path(__file__).resolve().parents[2]

    output_file = (
        root / "data" / "tracks" / "Aukštadvaris" / "blender" / "scene_transform.json"
    )

    orthophoto = get_orthophoto()

    track_centerline = get_track_centerline()

    orthophoto_data = export_orthophoto(
        orthophoto,
    )

    track_data = export_track_centerline(
        track_centerline,
    )

    scene_transform = create_scene_transform(
        orthophoto_data,
        track_data,
    )

    save_scene_transform(
        output_file,
        scene_transform,
    )

    print("Scene transform exported.")
