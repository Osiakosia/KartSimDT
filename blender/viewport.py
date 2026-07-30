from __future__ import annotations

import bpy


def reset_viewport() -> None:

    for area in bpy.context.screen.areas:

        if area.type != "VIEW_3D":
            continue

        space = area.spaces.active
        region = space.region_3d

        region.view_rotation = (
            1.0,
            0.0,
            0.0,
            0.0,
        )

        region.view_location = (
            0.0,
            0.0,
            0.0,
        )

        region.view_distance = 3.0
        region.view_perspective = "ORTHO"

        # Material Preview
        space.shading.type = "MATERIAL"
