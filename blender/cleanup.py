from __future__ import annotations

import bpy


def cleanup_scene() -> None:
    """
    Remove previous orthophoto meshes.
    Keep TrackCenterline and other non-mesh objects.
    """

    bpy.ops.object.select_all(action="DESELECT")

    for obj in list(bpy.data.objects):

        if obj.type != "MESH":
            continue

        obj.select_set(True)

    bpy.ops.object.delete()

    bpy.ops.outliner.orphans_purge()
