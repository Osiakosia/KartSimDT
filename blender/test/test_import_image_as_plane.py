from pathlib import Path

image_file = (
    Path(__file__).resolve().parents[2] / "data" / "orthophotos" / "Aukstadvaris.png"
)

print("=" * 60)
print("Testing Blender Image as Plane")
print("=" * 60)

print(image_file)
