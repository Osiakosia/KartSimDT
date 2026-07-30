"""
Export Blender scene transform.
"""

from __future__ import annotations

import json
from math import degrees
from pathlib import Path

import bpy


def main() -> None:
    root = Path(__file__).resolve().parents[2]

    output_file = (
        root / "data" / "tracks" / "Aukštadvaris" / "blender" / "scene_transform.json"
    )

    orthophoto = bpy.data.objects["Orthophoto"]
    centerline = bpy.data.objects["TrackSurvey"]

    scene_transform = {
        "orthophoto": {
            "scale": orthophoto.scale.x,
        },
        "track_centerline": {
            "scale": centerline.scale.x,
            "rotation_deg": degrees(
                centerline.rotation_euler.z,
            ),
            "offset_x": centerline.location.x,
            "offset_y": centerline.location.y,
            "offset_z": centerline.location.z,
        },
    }

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            scene_transform,
            file,
            indent=4,
        )

    print()
    print("=" * 60)
    print("SCENE TRANSFORM EXPORTED")
    print("=" * 60)
    print()

    print(output_file)

    print()
    print(
        json.dumps(
            scene_transform,
            indent=4,
        )
    )


if __name__ == "__main__":
    main()
