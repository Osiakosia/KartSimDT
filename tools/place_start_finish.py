"""
Interactive Start/Finish placement tool for KartSimDT.

Usage inside Blender:
    exec(compile(open(r"<project>/blender/tools/place_start_finish.py",
    encoding="utf-8").read(), "<place_start_finish.py>", "exec"))

Then run:
    bpy.ops.kartsimdt.place_start_finish('INVOKE_DEFAULT')

The operator:
- uses the Orthophoto mesh as the placement surface;
- records two mouse clicks representing the real S/F line endpoints;
- creates a preview line in world coordinates;
- saves track-local XY coordinates to:
      data/tracks/<track>/design/start_finish.json

The source TrackSurvey / TrackRoad / centerline data are not modified.
"""

from __future__ import annotations

import json
from pathlib import Path

import bpy
from bpy_extras import view3d_utils
from mathutils import Vector

OBJECT_NAME = "StartFinishLine"
ORTHOPHOTO_NAME = "Orthophoto"
OUTPUT_RELATIVE = Path("design") / "start_finish.json"


def project_root() -> Path:
    """Resolve KartSimDT project root from the current Blender file."""

    blend_path = Path(bpy.data.filepath).resolve()

    if not blend_path.name:
        raise RuntimeError("Save the Blender scene before placing Start/Finish.")


def track_root() -> Path:
    """Resolve the active track root from the current Blender file."""

    blend_path = Path(bpy.data.filepath).resolve()

    # <track>/blender/scene.blend
    return blend_path.parent.parent


def world_to_track_local(point: Vector) -> Vector:
    """
    Convert a Blender world-space point to the track-local coordinate system.

    Current scene_transform.json has the TrackSurvey transform applied as
    object transform. The initial implementation assumes track-local and
    Blender world XY are the same after the existing calibration.
    """

    return Vector((point.x, point.y, point.z))


def raycast_orthophoto(
    context: bpy.types.Context,
    event: bpy.types.Event,
) -> Vector | None:
    """Return the world-space hit point on the Orthophoto mesh."""

    region = context.region
    region_3d = context.space_data.region_3d

    mouse = (event.mouse_region_x, event.mouse_region_y)

    origin = view3d_utils.region_2d_to_origin_3d(
        region,
        region_3d,
        mouse,
    )
    direction = view3d_utils.region_2d_to_vector_3d(
        region,
        region_3d,
        mouse,
    )

    orthophoto = bpy.data.objects.get(ORTHOPHOTO_NAME)

    if orthophoto is None:
        raise RuntimeError(f"Required object '{ORTHOPHOTO_NAME}' was not found.")

    inverse = orthophoto.matrix_world.inverted()

    local_origin = inverse @ origin
    local_direction = (inverse.to_3x3() @ direction).normalized()

    hit, location, _normal, _face_index = orthophoto.ray_cast(
        local_origin,
        local_direction,
    )

    if not hit:
        return None

    return orthophoto.matrix_world @ location


def road_z_at_xy(point: Vector) -> float:
    """Return TrackRoad elevation at an XY position."""

    road = bpy.data.objects.get("TrackRoad")

    if road is None:
        return point.z

    inverse = road.matrix_world.inverted()

    origin_world = Vector((point.x, point.y, 1000.0))
    direction_world = Vector((0.0, 0.0, -1.0))

    origin_local = inverse @ origin_world
    direction_local = (inverse.to_3x3() @ direction_world).normalized()

    hit, location, _normal, _face_index = road.ray_cast(
        origin_local,
        direction_local,
    )

    if not hit:
        return point.z

    world_location = road.matrix_world @ location
    return world_location.z


def create_preview_line(
    point_a: Vector,
    point_b: Vector,
) -> bpy.types.Object:
    """Create or replace the S/F preview line on TrackRoad."""

    old = bpy.data.objects.get(OBJECT_NAME)

    if old is not None:
        bpy.data.objects.remove(old, do_unlink=True)

    curve_data = bpy.data.curves.new(
        name=f"{OBJECT_NAME}_Curve",
        type="CURVE",
    )
    curve_data.dimensions = "3D"

    spline = curve_data.splines.new("POLY")
    spline.points.add(1)

    z_a = road_z_at_xy(point_a) + 0.03
    z_b = road_z_at_xy(point_b) + 0.03

    spline.points[0].co = (
        point_a.x,
        point_a.y,
        z_a,
        1.0,
    )
    spline.points[1].co = (
        point_b.x,
        point_b.y,
        z_b,
        1.0,
    )

    curve_data.bevel_depth = 0.08
    curve_data.bevel_resolution = 2

    obj = bpy.data.objects.new(
        OBJECT_NAME,
        curve_data,
    )

    bpy.context.scene.collection.objects.link(obj)

    return obj


def save_placement(
    point_a: Vector,
    point_b: Vector,
) -> Path:
    """Persist S/F placement as track data."""

    local_a = world_to_track_local(point_a)
    local_b = world_to_track_local(point_b)

    center = (local_a + local_b) * 0.5

    direction = local_b - local_a
    length = direction.length

    if length <= 1e-9:
        raise ValueError("Start/Finish endpoints must not be identical.")

    direction.normalize()

    data = {
        "format": "KartSimDT Start Finish Placement",
        "version": 1,
        "placement": {
            "point_a": {
                "x": local_a.x,
                "y": local_a.y,
            },
            "point_b": {
                "x": local_b.x,
                "y": local_b.y,
            },
            "center": {
                "x": center.x,
                "y": center.y,
            },
            "direction": {
                "x": direction.x,
                "y": direction.y,
            },
            "length_m": length,
        },
    }

    output_file = track_root() / OUTPUT_RELATIVE
    output_file.parent.mkdir(parents=True, exist_ok=True)

    output_file.write_text(
        json.dumps(
            data,
            indent=2,
        ),
        encoding="utf-8",
    )

    return output_file


class KARTSIMDT_OT_place_start_finish(bpy.types.Operator):
    """Place Start/Finish line using the orthophoto."""

    bl_idname = "kartsimdt.place_start_finish"
    bl_label = "Place KartSimDT Start/Finish"
    bl_options = {"REGISTER", "UNDO"}

    point_a: Vector | None = None

    def invoke(
        self,
        context: bpy.types.Context,
        event: bpy.types.Event,
    ):
        if context.area is None or context.area.type != "VIEW_3D":
            self.report(
                {"ERROR"},
                "Run Start/Finish placement from a 3D Viewport.",
            )
            return {"CANCELLED"}

        if bpy.data.objects.get(ORTHOPHOTO_NAME) is None:
            self.report(
                {"ERROR"},
                "Orthophoto object not found.",
            )
            return {"CANCELLED"}

        self.point_a = None

        context.window_manager.modal_handler_add(self)

        self.report(
            {"INFO"},
            "Click first S/F endpoint, then second endpoint. ESC cancels.",
        )

        return {"RUNNING_MODAL"}

    def modal(
        self,
        context: bpy.types.Context,
        event: bpy.types.Event,
    ):
        if event.type in {"ESC", "RIGHTMOUSE"}:
            self.report({"INFO"}, "Start/Finish placement cancelled.")
            return {"CANCELLED"}

        if event.type == "LEFTMOUSE" and event.value == "PRESS":
            try:
                point = raycast_orthophoto(
                    context,
                    event,
                )
            except RuntimeError as exc:
                self.report({"ERROR"}, str(exc))
                return {"CANCELLED"}

            if point is None:
                self.report(
                    {"WARNING"},
                    "No Orthophoto surface under cursor.",
                )
                return {"RUNNING_MODAL"}

            if self.point_a is None:
                self.point_a = point

                self.report(
                    {"INFO"},
                    (
                        f"First endpoint: "
                        f"X={point.x:.3f} Y={point.y:.3f}. "
                        "Click second endpoint."
                    ),
                )

                return {"RUNNING_MODAL"}

            point_b = point

            try:
                output_file = save_placement(
                    self.point_a,
                    point_b,
                )

                create_preview_line(
                    self.point_a,
                    point_b,
                )
            except (OSError, ValueError) as exc:
                self.report({"ERROR"}, str(exc))
                return {"CANCELLED"}

            self.report(
                {"INFO"},
                f"Start/Finish saved: {output_file}",
            )

            return {"FINISHED"}

        return {"RUNNING_MODAL"}


def register() -> None:
    """Register the placement operator."""

    bpy.utils.register_class(
        KARTSIMDT_OT_place_start_finish,
    )


def unregister() -> None:
    """Unregister the placement operator."""

    bpy.utils.unregister_class(
        KARTSIMDT_OT_place_start_finish,
    )


if __name__ == "__main__":
    register()
