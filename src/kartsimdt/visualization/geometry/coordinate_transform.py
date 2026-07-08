"""
coordinate_transform.py

Transforms GPS coordinates into the local engineering
coordinate system.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.point import Point
from kartsimdt.visualization.geometry.point import LocalPoint
from kartsimdt.visualization.geometry.reference_frame import (
    LocalReferenceFrame,
)


class CoordinateTransform:
    """
    Converts GPS coordinates into the local engineering
    coordinate system.
    """

    def transform(
        self,
        point: Point,
        frame: LocalReferenceFrame,
    ) -> LocalPoint:
        """
        Transform one GPS point into local coordinates.
        """

        delta_longitude = point.longitude - frame.origin_longitude

        delta_latitude = point.latitude - frame.origin_latitude

        origin_elevation = frame.origin_elevation

        point_elevation = (
            point.elevation if point.elevation is not None else origin_elevation
        )

        x = delta_longitude * frame.metres_per_degree_longitude

        y = delta_latitude * frame.metres_per_degree_latitude

        z = point_elevation - origin_elevation

        return LocalPoint(
            x=x,
            y=y,
            z=z,
        )
