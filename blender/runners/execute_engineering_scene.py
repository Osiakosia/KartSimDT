from __future__ import annotations

import sys
from pathlib import Path

import bpy

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ROOT),
    )


def print_scene_objects(
    title: str,
) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    for obj in bpy.context.scene.objects:
        print(f"{obj.name:25} " f"{obj.type:8} " f"library={obj.library}")


print("=" * 60)
print("KartSimDT Blender Runner")
print("=" * 60)

print(f"Project Root : {ROOT}")
print(f"Blend File   : {bpy.data.filepath}")

# Configure KartSimDT addon for headless execution.
prefs = bpy.context.preferences.addons["kartsimdt"].preferences
prefs.project_root = str(ROOT)

print(f"Addon Project Root : {prefs.project_root}")

print_scene_objects(
    "SCENE BEFORE OPERATOR",
)

print()
print("Executing:")
print("  bpy.ops.kartsimdt.build_engineering_scene()")

result = bpy.ops.kartsimdt.build_engineering_scene()


bpy.ops.wm.save_as_mainfile(
    filepath=bpy.data.filepath,
)

print(f"Scene saved: {bpy.data.filepath}")

survey = bpy.data.objects.get("TrackSurvey")
road = bpy.data.objects.get("TrackRoad")

if survey is not None:
    points = [survey.matrix_world @ point.co for point in survey.data.splines[0].points]

    print(
        "TrackSurvey WORLD Z:",
        min(point.z for point in points),
        "->",
        max(point.z for point in points),
    )

if road is not None:
    z_values = [(road.matrix_world @ vertex.co).z for vertex in road.data.vertices]

    print(
        "TrackRoad WORLD Z:",
        min(z_values),
        "->",
        max(z_values),
    )

print()
print("Operator Result:", result)

print_scene_objects(
    "SCENE AFTER OPERATOR",
)

print("=" * 60)
