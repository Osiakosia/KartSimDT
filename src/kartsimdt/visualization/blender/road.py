"""
Blender road mesh writer.

Converts a generated RoadMesh into a Blender mesh object.
"""

from __future__ import annotations

import bpy

from kartsimdt.track.road_geometry import RoadMesh


class BlenderRoadWriter:
    """Write RoadMesh geometry into Blender."""

    def create(
        self,
        road_mesh: RoadMesh,
        name: str = "TrackRoad_TEST",
    ) -> bpy.types.Object:
        """Create a Blender mesh object from RoadMesh."""

        mesh = bpy.data.meshes.new(f"{name}_Mesh")

        vertices = [(point.x, point.y, point.z) for point in road_mesh.vertices]

        mesh.from_pydata(
            vertices,
            [],
            road_mesh.faces,
        )

        mesh.update()

        obj = bpy.data.objects.new(name, mesh)

        bpy.context.collection.objects.link(obj)

        return obj
