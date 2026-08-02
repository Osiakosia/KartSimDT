"""
Google Earth orthophoto calibration helper.

Purpose
-------
Import a Google Earth reference image into Blender using
pixel dimensions as Blender dimensions.

This creates a diagnostic plane where:

    1 image pixel = 1 Blender unit

The Blender Measure tool can then be used to measure pixel
distances between known Google Earth reference points.

This script does NOT modify production orthophoto calibration.
"""

from __future__ import annotations

from pathlib import Path

import bpy

OBJECT_NAME = "GoogleEarthCalibration"
MATERIAL_NAME = "GoogleEarthCalibration"


def get_project_root() -> Path:
    """
    Return KartSimDT project root.
    """

    return Path(__file__).resolve().parents[2]


def get_image_file() -> Path:
    """
    Return Google Earth calibration image path.
    """

    root = get_project_root()

    return (
        root
        / "data"
        / "tracks"
        / "Aukštadvaris"
        / "google_earth"
        / "Aukstadvaris_200m_x_y_kalibracija.png"
    )


def remove_existing_object() -> None:
    """
    Remove previous calibration object if it exists.
    """

    obj = bpy.data.objects.get(OBJECT_NAME)

    if obj is not None:
        bpy.data.objects.remove(
            obj,
            do_unlink=True,
        )


def load_image(
    image_file: Path,
) -> bpy.types.Image:
    """
    Load Google Earth calibration image.
    """

    if not image_file.exists():
        raise FileNotFoundError(f"Calibration image not found: {image_file}")

    image = bpy.data.images.load(
        str(image_file),
        check_existing=True,
    )

    return image


def create_plane(
    image: bpy.types.Image,
) -> bpy.types.Object:
    """
    Create plane using image pixel dimensions.

    1 pixel = 1 Blender unit.
    """

    width_px = int(image.size[0])
    height_px = int(image.size[1])

    bpy.ops.mesh.primitive_plane_add(
        size=2.0,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
    )

    plane = bpy.context.active_object

    if plane is None:
        raise RuntimeError("Failed to create calibration plane.")

    plane.name = OBJECT_NAME

    # Blender primitive plane is 2 x 2 units.
    # Therefore:
    #
    # scale.x = width_px / 2
    # scale.y = height_px / 2
    #
    # gives final dimensions exactly equal to image pixels.

    plane.scale.x = width_px / 2.0
    plane.scale.y = height_px / 2.0
    plane.scale.z = 1.0

    # Apply scale so:
    #
    # Dimensions = image pixel dimensions
    # Scale      = (1, 1, 1)

    bpy.context.view_layer.objects.active = plane
    plane.select_set(True)

    bpy.ops.object.transform_apply(
        location=False,
        rotation=False,
        scale=True,
    )

    return plane


def create_material(
    image: bpy.types.Image,
) -> bpy.types.Material:
    """
    Create material containing the Google Earth image.
    """

    old_material = bpy.data.materials.get(MATERIAL_NAME)

    if old_material is not None:
        bpy.data.materials.remove(
            old_material,
            do_unlink=True,
        )

    material = bpy.data.materials.new(
        name=MATERIAL_NAME,
    )

    material.use_nodes = True

    node_tree = material.node_tree

    if node_tree is None:
        raise RuntimeError("Material node tree was not created.")

    nodes = node_tree.nodes
    links = node_tree.links

    nodes.clear()

    texture = nodes.new(
        "ShaderNodeTexImage",
    )

    texture.name = "Google Earth Image"
    texture.image = image
    texture.interpolation = "Closest"
    texture.location = (-500.0, 0.0)

    bsdf = nodes.new(
        "ShaderNodeBsdfPrincipled",
    )

    bsdf.location = (-100.0, 0.0)

    output = nodes.new(
        "ShaderNodeOutputMaterial",
    )

    output.location = (250.0, 0.0)

    links.new(
        texture.outputs["Color"],
        bsdf.inputs["Base Color"],
    )

    links.new(
        bsdf.outputs["BSDF"],
        output.inputs["Surface"],
    )

    return material


def assign_material(
    plane: bpy.types.Object,
    material: bpy.types.Material,
) -> None:
    """
    Assign calibration material to plane.
    """

    plane.data.materials.clear()
    plane.data.materials.append(material)


def print_report(
    image_file: Path,
    image: bpy.types.Image,
    plane: bpy.types.Object,
) -> None:
    """
    Print calibration plane information.
    """

    print()
    print("=" * 70)
    print("GOOGLE EARTH CALIBRATION")
    print("=" * 70)

    print()
    print("Image")
    print(f"File       : {image_file}")
    print(f"Pixels     : {image.size[0]} x {image.size[1]}")

    print()
    print("Plane")
    print(f"Name       : {plane.name}")
    print(f"Dimensions : {plane.dimensions[:]}")
    print(f"Location   : {plane.location[:]}")
    print(f"Rotation   : {plane.rotation_euler[:]}")
    print(f"Scale      : {plane.scale[:]}")

    print()
    print("Coordinate rule:")
    print("    1 Blender unit = 1 image pixel")

    print()
    print("Known Google Earth references:")
    print("    X reference = 200.32 m")
    print("    Y reference = 200.04 m")

    print()
    print("Measure the SAME reference lines in Blender.")
    print()
    print("Then calculate:")
    print("    metres_per_pixel_x = 200.32 / measured_x")
    print("    metres_per_pixel_y = 200.04 / measured_y")

    print()
    print("=" * 70)


def main() -> None:
    """
    Build Google Earth calibration scene.
    """

    image_file = get_image_file()

    remove_existing_object()

    image = load_image(
        image_file,
    )

    plane = create_plane(
        image,
    )

    material = create_material(
        image,
    )

    assign_material(
        plane,
        material,
    )

    print_report(
        image_file,
        image,
        plane,
    )


if __name__ == "__main__":
    main()
