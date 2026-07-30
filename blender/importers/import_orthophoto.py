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

    print("Orthophoto dimensions:", plane.dimensions)
    print("Orthophoto location:", plane.location)

    print("Track location:", curve.location)
    print("Track bounds:", curve.bound_box)


def create_orthophoto_plane(
    image: bpy.types.Image,
) -> bpy.types.Object:
    """
    Create orthophoto plane with correct aspect ratio.
    """

    bpy.ops.mesh.primitive_plane_add(
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0),
    )

    plane = bpy.context.active_object
    plane.name = "Orthophoto"

    width = image.size[0]
    height = image.size[1]

    aspect = width / height

    if aspect >= 1.0:
        plane.scale.x = aspect
        plane.scale.y = 1.0
    else:
        plane.scale.x = 1.0
        plane.scale.y = 1.0 / aspect

    print()
    print("Plane created")
    print(f"Image size : {width} x {height}")
    print(f"Aspect     : {aspect:.6f}")
    print(f"Dimensions : {plane.dimensions}")

    return plane


def apply_orthophoto_transform(
    plane: bpy.types.Object,
    transform: dict,
) -> None:
    """
    Apply Orthophoto transform.
    """

    print("Transform dict:", transform)
    print("Transform scale:", transform["scale"])

    plane.scale.x *= transform["scale"]
    plane.scale.y *= transform["scale"]

    print("Scale before apply:", plane.scale[:])

    bpy.context.view_layer.objects.active = plane

    bpy.ops.object.transform_apply(
        location=False,
        rotation=False,
        scale=True,
    )

    print("Scale after apply:", plane.scale[:])

    print()
    print("ORTHOPHOTO TRANSFORM")
    print(f"Scale      : {plane.scale[:]}")
    print(f"Dimensions : {plane.dimensions[:]}")
    print(f"Location   : {plane.location[:]}")


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

    image_file = track_folder / "google_earth" / "orthophoto.png"

    transform_file = track_folder / "blender" / "scene_transform.json"

    with transform_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        scene_transform = json.load(file)

    image = load_orthophoto(
        image_file,
    )

    orthophoto = scene_transform["orthophoto"]

    plane = create_orthophoto_plane(
        image=image,
    )

    apply_orthophoto_transform(
        plane,
        orthophoto,
    )

    print(dir(bpy.ops))

    print(dir(bpy.ops.import_image))

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
