"""
Tests for CoordinateTransform.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.point import Point
from kartsimdt.visualization.geometry.coordinate_transform import (
    CoordinateTransform,
)
from kartsimdt.visualization.geometry.reference_frame import (
    LocalReferenceFrame,
)


def create_reference_frame() -> LocalReferenceFrame:
    return LocalReferenceFrame(
        origin_longitude=24.0,
        origin_latitude=55.0,
        origin_elevation=100.0,
        metres_per_degree_latitude=111320.0,
        metres_per_degree_longitude=63850.0,
    )


def test_origin_maps_to_zero() -> None:

    transformer = CoordinateTransform()

    frame = create_reference_frame()

    point = Point(
        longitude=24.0,
        latitude=55.0,
        elevation=100.0,
    )

    local = transformer.transform(point, frame)

    assert local.x == 0.0
    assert local.y == 0.0
    assert local.z == 0.0


def test_longitude_maps_to_x() -> None:

    transformer = CoordinateTransform()

    frame = create_reference_frame()

    point = Point(
        longitude=24.001,
        latitude=55.0,
        elevation=100.0,
    )

    local = transformer.transform(point, frame)

    assert local.x > 0.0


def test_latitude_maps_to_y() -> None:

    transformer = CoordinateTransform()

    frame = create_reference_frame()

    point = Point(
        longitude=24.0,
        latitude=55.001,
        elevation=100.0,
    )

    local = transformer.transform(point, frame)

    assert local.y > 0.0


def test_elevation_maps_to_z() -> None:

    transformer = CoordinateTransform()

    frame = create_reference_frame()

    point = Point(
        longitude=24.0,
        latitude=55.0,
        elevation=105.0,
    )

    local = transformer.transform(point, frame)

    assert local.z == 5.0
