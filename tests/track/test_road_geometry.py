import pytest

from kartsimdt.track.design import RoadDesign, WidthZone
from kartsimdt.track.road_geometry import (
    Point3D,
    RoadGeometryGenerator,
)
from kartsimdt.track.road_width import RoadWidthResolver


def create_resolver() -> RoadWidthResolver:
    design = RoadDesign(
        default_width_m=8.0,
        width_zones=[
            WidthZone(
                name="start_finish",
                start_index=2,
                end_index=3,
                width_m=11.0,
            )
        ],
    )

    return RoadWidthResolver(design)


def test_generates_two_vertices_per_centerline_point() -> None:
    centerline = [
        Point3D(0.0, 0.0, 0.0),
        Point3D(10.0, 0.0, 0.0),
        Point3D(10.0, 10.0, 0.0),
        Point3D(0.0, 10.0, 0.0),
    ]

    generator = RoadGeometryGenerator(
        centerline=centerline,
        width_resolver=create_resolver(),
    )

    mesh = generator.generate()

    assert len(mesh.vertices) == 8
    assert len(mesh.faces) == 4


def test_default_width_is_used() -> None:
    centerline = [
        Point3D(0.0, 0.0, 0.0),
        Point3D(10.0, 0.0, 0.0),
        Point3D(10.0, 10.0, 0.0),
        Point3D(0.0, 10.0, 0.0),
    ]

    generator = RoadGeometryGenerator(
        centerline=centerline,
        width_resolver=create_resolver(),
    )

    mesh = generator.generate()

    # P0 uses the default 8 m width.
    left = mesh.vertices[0]
    right = mesh.vertices[1]

    width = (
        (left.x - right.x) ** 2 + (left.y - right.y) ** 2 + (left.z - right.z) ** 2
    ) ** 0.5

    assert width == pytest.approx(8.0)


def test_start_finish_width_is_used() -> None:
    centerline = [
        Point3D(0.0, 0.0, 0.0),
        Point3D(10.0, 0.0, 0.0),
        Point3D(10.0, 10.0, 0.0),
        Point3D(0.0, 10.0, 0.0),
    ]

    generator = RoadGeometryGenerator(
        centerline=centerline,
        width_resolver=create_resolver(),
    )

    mesh = generator.generate()

    # P2 uses the 11 m width zone.
    left = mesh.vertices[4]
    right = mesh.vertices[5]

    width = (
        (left.x - right.x) ** 2 + (left.y - right.y) ** 2 + (left.z - right.z) ** 2
    ) ** 0.5

    assert width == pytest.approx(11.0)
