"""
Import orthophoto into Blender.
"""

from __future__ import annotations

import json
from pathlib import Path

import bpy

# print("Blender version:", bpy.app.version_string)

# print()
#
# print("Testing operator...")
#
# print(hasattr(bpy.ops, "import_image"))
#
# print(dir(bpy.ops))


def load_orthophoto(
    image_file: Path,
) -> bpy.types.Image:
    """
    Load orthophoto image.
    """

    return bpy.data.images.load(
        str(image_file),
    )


def create_orthophoto_plane(
    image: bpy.types.Image,
    calibration: dict,
) -> bpy.types.Object:
    """
    Create orthophoto plane in calibrated real-world dimensions.
    """

    image_width_px = image.size[0]
    image_height_px = image.size[1]

    metres_per_pixel_x = calibration["metres_per_pixel_x"]
    metres_per_pixel_y = calibration["metres_per_pixel_y"]

    width_m = image_width_px * metres_per_pixel_x
    height_m = image_height_px * metres_per_pixel_y

    bpy.ops.mesh.primitive_plane_add(
        size=2.0,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
    )

    plane = bpy.context.active_object
    plane.name = "Orthophoto"

    plane.dimensions = (
        width_m,
        height_m,
        0.0,
    )

    bpy.context.view_layer.update()

    bpy.context.view_layer.objects.active = plane

    bpy.ops.object.transform_apply(
        location=False,
        rotation=False,
        scale=True,
    )

    print()
    print("=" * 60)
    print("ORTHOPHOTO METRIC CALIBRATION")
    print("=" * 60)

    print(f"Image size         : {image_width_px} x {image_height_px} px")
    print(f"Metres/pixel X     : {metres_per_pixel_x:.8f}")
    print(f"Metres/pixel Y     : {metres_per_pixel_y:.8f}")
    print(f"Width              : {width_m:.3f} m")
    print(f"Height             : {height_m:.3f} m")
    print(f"Dimensions         : {plane.dimensions[:]}")
    print(f"Object scale       : {plane.scale[:]}")

    return plane


# def create_orthophoto_plane(
#     image: bpy.types.Image,
#     calibration: dict,
# ) -> bpy.types.Object:
#     """
#     Create orthophoto plane in real-world metric dimensions.
#     """
#
#     image_width_px = image.size[0]
#     image_height_px = image.size[1]
#
#     metres_per_pixel_x = calibration["metres_per_pixel_x"]
#     metres_per_pixel_y = calibration["metres_per_pixel_y"]
#
#     width_m = image_width_px * metres_per_pixel_x
#     height_m = image_height_px * metres_per_pixel_y
#
#     bpy.ops.mesh.primitive_plane_add(
#         size=2.0,
#         location=(0.0, 0.0, 0.0),
#         rotation=(0.0, 0.0, 0.0),
#     )
#
#     plane = bpy.context.active_object
#     plane.name = "Orthophoto"
#
#     plane.dimensions.x = width_m
#     plane.dimensions.y = height_m
#
#     bpy.context.view_layer.objects.active = plane
#
#     bpy.ops.object.transform_apply(
#         location=False,
#         rotation=False,
#         scale=True,
#     )
#
#     print()
#     print("=" * 60)
#     print("ORTHOPHOTO REAL-WORLD CALIBRATION")
#     print("=" * 60)
#     print(
#         f"Image size       : "
#         f"{image_width_px} x {image_height_px} px"
#     )
#     print(
#         f"Metres/pixel X   : "
#         f"{metres_per_pixel_x:.9f}"
#     )
#     print(
#         f"Metres/pixel Y   : "
#         f"{metres_per_pixel_y:.9f}"
#     )
#     print(f"Width            : {width_m:.3f} m")
#     print(f"Height           : {height_m:.3f} m")
#     print(f"Dimensions       : {plane.dimensions[:]}")
#     print(f"Scale            : {plane.scale[:]}")
#
#     return plane

# def create_orthophoto_plane(
#     image: bpy.types.Image,
# ) -> bpy.types.Object:
#     """
#     Create orthophoto plane in real-world metric dimensions.
#     """
#
#     # Photoshop reference measurement:
#     # 56 px = 8 m
#     metres_per_pixel = 8.0 / 56.0
#
#     image_width_px = 2880
#     image_height_px = 1501
#
#     width_m = image_width_px * metres_per_pixel
#     height_m = image_height_px * metres_per_pixel
#
#     bpy.ops.mesh.primitive_plane_add(
#         size=2.0,
#         location=(0.0, 0.0, 0.0),
#         rotation=(0.0, 0.0, 0.0),
#     )
#
#     plane = bpy.context.active_object
#     plane.name = "Orthophoto"
#
#     plane.dimensions.x = width_m
#     plane.dimensions.y = height_m
#
#     bpy.context.view_layer.objects.active = plane
#
#     bpy.ops.object.transform_apply(
#         location=False,
#         rotation=False,
#         scale=True,
#     )
#
#     print()
#     print("Plane created")
#     print(f"Image size       : {image_width_px} x {image_height_px} px")
#     print(f"Reference        : 56 px = 8 m")
#     print(f"Metres per pixel : {metres_per_pixel:.9f}")
#     print(f"Width            : {width_m:.3f} m")
#     print(f"Height           : {height_m:.3f} m")
#     print(f"Dimensions       : {plane.dimensions[:]}")
#     print(f"Scale            : {plane.scale[:]}")
#
#     return plane

# def create_orthophoto_plane(
#     image: bpy.types.Image,
# ) -> bpy.types.Object:
#     """
#     Create orthophoto plane with correct aspect ratio.
#     """
#
#     bpy.ops.mesh.primitive_plane_add(
#         location=(0.0, 0.0, 0.0),
#         rotation=(0.0, 0.0, 0.0),
#     )
#
#     plane = bpy.context.active_object
#     plane.name = "Orthophoto"
#
#     width = image.size[0]
#     height = image.size[1]
#
#     aspect = width / height
#
#     if aspect >= 1.0:
#         plane.scale.x = aspect
#         plane.scale.y = 1.0
#     else:
#         plane.scale.x = 1.0
#         plane.scale.y = 1.0 / aspect
#
#     print()
#     print("Plane created")
#     print(f"Image size : {width} x {height}")
#     print(f"Aspect     : {aspect:.6f}")
#     print(f"Dimensions : {plane.dimensions}")
#
#     return plane


def apply_orthophoto_transform(
    plane: bpy.types.Object,
    transform: dict,
) -> None:
    """
    Apply Orthophoto scene transform.
    """

    scale = transform["scale"]

    plane.scale.x *= scale
    plane.scale.y *= scale

    plane.rotation_euler.z = transform["rotation"]

    plane.location.x = transform["offset_x"]
    plane.location.y = transform["offset_y"]

    print()
    print("=" * 60)
    print("ORTHOPHOTO SCENE TRANSFORM")
    print("=" * 60)
    print(f"Scale      : {scale}")
    print(f"Rotation   : {transform['rotation']}")
    print(f"Offset X   : {transform['offset_x']}")
    print(f"Offset Y   : {transform['offset_y']}")
    print(f"Location   : {plane.location[:]}")
    print(f"Dimensions : {plane.dimensions[:]}")


def create_orthophoto_material(
    image: bpy.types.Image,
) -> bpy.types.Material:
    """
    Create orthophoto material.
    """

    material = bpy.data.materials.new(
        name="Orthophoto",
    )

    material.use_nodes = True

    return material


def assign_material(
    plane: bpy.types.Object,
    material: bpy.types.Material,
) -> None:
    """
    Assign material to plane.
    """

    if plane.data.materials:
        plane.data.materials[0] = material
    else:
        plane.data.materials.append(material)


def create_texture_nodes(
    material: bpy.types.Material,
    image: bpy.types.Image,
) -> None:
    """
    Add image texture to existing material.
    """

    node_tree = material.node_tree
    assert node_tree is not None

    nodes = node_tree.nodes
    links = node_tree.links

    # Surandame esamus mazgus
    bsdf = nodes.get("Principled BSDF")
    output = nodes.get("Material Output")

    if bsdf is None:
        bsdf = nodes.new("ShaderNodeBsdfPrincipled")

    if output is None:
        output = nodes.new("ShaderNodeOutputMaterial")

    # Pašaliname tik seną Image Texture
    old = nodes.get("Image Texture")
    if old is not None:
        nodes.remove(old)

    # Sukuriame naują Image Texture
    texture = nodes.new("ShaderNodeTexImage")
    texture.name = "Image Texture"
    texture.image = image

    # Patogus išdėstymas
    texture.location = (-500, 0)
    bsdf.location = (0, 0)
    output.location = (300, 0)

    # Išvalome tik Base Color jungtis
    for link in list(links):
        if link.to_node == bsdf and link.to_socket.name == "Base Color":
            links.remove(link)

    # Sukuriame jungtis
    links.new(
        texture.outputs["Color"],
        bsdf.inputs["Base Color"],
    )

    # BSDF -> Output jungtis
    connected = False

    for link in links:
        if link.from_node == bsdf and link.to_node == output:
            connected = True
            break

    if not connected:
        links.new(
            bsdf.outputs["BSDF"],
            output.inputs["Surface"],
        )

    print()
    print("=" * 60)
    print("NODE TREE")
    print("=" * 60)

    for node in nodes:
        print(f"{node.name:20} {node.location}")

    print()

    for link in links:
        print(f"{link.from_node.name}" f" -> " f"{link.to_node.name}")


def import_orthophoto() -> bpy.types.Object:
    """
    Import orthophoto.
    """

    root = Path(__file__).resolve().parents[2]

    track_folder = root / "data" / "tracks" / "Aukštadvaris"

    calibration_file = track_folder / "google_earth" / "calibration.json"

    transform_file = track_folder / "blender" / "scene_transform.json"

    # 1. Load calibration first
    with calibration_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        calibration = json.load(file)

    orthophoto = calibration["orthophoto"]

    with transform_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        scene_transform = json.load(file)

    orthophoto_transform = scene_transform["orthophoto"]

    # 2. Get image filename from calibration.json
    image_file = track_folder / "google_earth" / orthophoto["source_image"]

    print()
    print("=" * 60)
    print("ORTHOPHOTO SOURCE")
    print("=" * 60)
    print(f"Calibration file : {calibration_file}")
    print(f"Image file       : {image_file}")

    # 3. Load image
    image = load_orthophoto(
        image_file,
    )

    # 4. Create calibrated plane
    plane = create_orthophoto_plane(
        image=image,
        calibration=orthophoto,
    )

    # 5. Apply saved scene transform
    apply_orthophoto_transform(
        plane,
        orthophoto_transform,
    )

    print()
    print("Active Object")
    print(bpy.context.active_object)

    print()

    print("Scene Objects")

    for obj in bpy.context.scene.objects:
        print(f"{obj.name} : {obj.type}")

    material = create_orthophoto_material(image)

    assign_material(
        plane,
        material,
    )

    print()
    print("===== MATERIAL DEBUG =====")
    print("Active material:", plane.active_material)
    print("Material slots:", len(plane.data.materials))

    if plane.data.materials:
        print("First slot:", plane.data.materials[0].name)
    else:
        print("First slot: EMPTY")

    create_texture_nodes(
        material,
        image,
    )

    print("\nLinks")

    for link in material.node_tree.links:
        print(
            link.from_node.name,
            "->",
            link.to_node.name,
            "|",
            link.from_socket.name,
            "->",
            link.to_socket.name,
        )

        print()

        print("UV Layers")

        for uv in plane.data.uv_layers:
            print(uv.name)

    print("\nNode positions")

    for node in material.node_tree.nodes:
        print(node.name, node.location)

    print()
    print("=" * 60)
    print("ORTHOPHOTO DEBUG")
    print("=" * 60)

    print()

    print("Image")
    print(f"Name      : {image.name}")
    print(f"Path      : {image.filepath}")
    print(f"Size      : {image.size[:]}")

    print()

    print("Plane")
    print(f"Name      : {plane.name}")
    print(f"Location  : {plane.location[:]}")
    print(f"Rotation  : {plane.rotation_euler[:]}")
    print(f"Scale     : {plane.scale[:]}")

    print()

    print("Material")
    print(f"Name      : {material.name}")
    print(f"Use Nodes : {material.use_nodes}")

    print()

    print("Material Slots")

    for slot in plane.material_slots:
        print(slot.material.name if slot.material else "EMPTY")

    print()

    print("Nodes")

    for node in material.node_tree.nodes:
        print(f"{node.name:20} {node.bl_idname}")

    print()

    texture = material.node_tree.nodes.get("Image Texture")

    if texture is not None:
        print("Texture Image")

        if texture.image is not None:
            print(texture.image.name)
            print(texture.image.filepath)
            print(texture.image.size[:])
        else:
            print("NONE")

        print()
        print("Object Active Material")
        print(plane.active_material)

        print("Rotation:", plane.rotation_euler)
        print("Scale:", plane.scale)
        print("Dimensions:", plane.dimensions)
        print("Matrix world:")
        print(plane.matrix_world)

        print()
        print("Object Mode")
        print(plane.mode)

        print("Current blend:")
        print(bpy.data.filepath)

        bpy.ops.object.shade_smooth()

        return plane


def main() -> None:
    import_orthophoto()


if __name__ == "__main__":
    main()
