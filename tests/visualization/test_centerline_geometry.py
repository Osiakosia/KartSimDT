"""
Tests for CenterlineGeometry.
"""

from __future__ import annotations

from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)
from kartsimdt.visualization.geometry.point import LocalPoint


def test_centerline_geometry_creates_empty() -> None:
    """
    CenterlineGeometry can be created with no points.
    """

    geometry = CenterlineGeometry(
        name="Test Track",
        points=[],
    )

    assert geometry.name == "Test Track"
    assert geometry.points == []


def test_centerline_geometry_stores_points() -> None:
    """
    CenterlineGeometry stores LocalPoint objects.
    """

    points = [
        LocalPoint(0.0, 0.0, 0.0),
        LocalPoint(1.0, 2.0, 0.0),
    ]

    geometry = CenterlineGeometry(
        name="Test Track",
        points=points,
    )

    assert len(geometry.points) == 2


def test_centerline_geometry_first_point() -> None:
    """
    First point is preserved.
    """

    points = [
        LocalPoint(0.0, 0.0, 0.0),
        LocalPoint(1.0, 2.0, 0.0),
    ]

    geometry = CenterlineGeometry(
        name="Test Track",
        points=points,
    )

    first = geometry.points[0]

    assert first.x == 0.0
    assert first.y == 0.0
    assert first.z == 0.0


def test_centerline_geometry_last_point() -> None:
    """
    Last point is preserved.
    """

    points = [
        LocalPoint(0.0, 0.0, 0.0),
        LocalPoint(5.0, 10.0, 0.0),
    ]

    geometry = CenterlineGeometry(
        name="Test Track",
        points=points,
    )

    last = geometry.points[-1]

    assert last.x == 5.0
    assert last.y == 10.0
    assert last.z == 0.0
