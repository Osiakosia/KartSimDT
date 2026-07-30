from pathlib import Path

import bpy

image_file = (
    Path(__file__).resolve().parents[2] / "data" / "orthophotos" / "Aukstadvaris.png"
)

print("Importing:", image_file)

result = bpy.ops.import_image.to_plane(
    files=[{"name": image_file.name}],
    directory=str(image_file.parent),
)

print(result)

print("Active:", bpy.context.active_object)
