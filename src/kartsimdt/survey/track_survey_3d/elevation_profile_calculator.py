"""
elevation_profile_calculator.py

Calculates distance and elevation information
along a Track Survey centerline.
"""

from __future__ import annotations

from dataclasses import dataclass

from kartsimdt.survey.track_survey.centerline import Centerline


@dataclass(slots=True)
class ElevationProfilePoint:
    """
    One point of an elevation profile.
    """

    distance_metres: float
    elevation: float
    delta_elevation: float
    grade_percent: float


class ElevationProfileCalculator:
    """
    Calculates an elevation profile from a track centerline.
    """

    def calculate(
        self,
        centerline: Centerline,
    ) -> list[ElevationProfilePoint]:
        """
        Calculate cumulative distance and elevation changes.
        """

        if centerline.count() == 0:
            return []

        points = centerline.points

        result: list[ElevationProfilePoint] = []

        distance = 0.0
        previous_elevation = points[0].elevation

        if previous_elevation is None:
            raise ValueError("Centerline point elevation must not be None.")

        result.append(
            ElevationProfilePoint(
                distance_metres=0.0,
                elevation=previous_elevation,
                delta_elevation=0.0,
                grade_percent=0.0,
            )
        )
        for previous, current in zip(
            points,
            points[1:],
            strict=False,
        ):
            if previous.elevation is None:
                raise ValueError("Centerline point elevation must not be None.")

            if current.elevation is None:
                raise ValueError("Centerline point elevation must not be None.")

            segment_distance = self._distance_metres(
                previous.latitude,
                previous.longitude,
                current.latitude,
                current.longitude,
            )

            distance += segment_distance

            delta_elevation = current.elevation - previous_elevation

            if segment_distance > 0.0:
                grade_percent = delta_elevation / segment_distance * 100.0
            else:
                grade_percent = 0.0

            result.append(
                ElevationProfilePoint(
                    distance_metres=distance,
                    elevation=current.elevation,
                    delta_elevation=delta_elevation,
                    grade_percent=grade_percent,
                )
            )

            previous_elevation = current.elevation

        return result

    @staticmethod
    def _distance_metres(
        latitude_1: float,
        longitude_1: float,
        latitude_2: float,
        longitude_2: float,
    ) -> float:
        """
        Calculate approximate WGS84 surface distance.

        Uses the haversine formula.
        """

        from math import asin, cos, radians, sin, sqrt

        earth_radius_metres = 6_371_000.0

        lat1 = radians(latitude_1)
        lat2 = radians(latitude_2)

        delta_lat = radians(latitude_2 - latitude_1)
        delta_lon = radians(longitude_2 - longitude_1)

        a = (
            sin(delta_lat / 2.0) ** 2
            + cos(lat1) * cos(lat2) * sin(delta_lon / 2.0) ** 2
        )

        return 2.0 * earth_radius_metres * asin(sqrt(a))
