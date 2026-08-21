"""
centerline_distance_calculator.py

Calculates cumulative distance along a Track Survey centerline.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

from kartsimdt.survey.track_survey.session import TrackSurveySession

EARTH_RADIUS_METRES = 6_371_000.0


@dataclass(frozen=True, slots=True)
class CenterlineDistancePoint:
    """
    Cumulative distance for one centerline survey point.
    """

    survey_index: int
    distance_metres: float


class CenterlineDistanceCalculator:
    """
    Calculates cumulative geodesic distance along
    a Track Survey centerline.
    """

    def calculate(
        self,
        survey: TrackSurveySession,
    ) -> tuple[CenterlineDistancePoint, ...]:
        points = survey.centerline.points

        if not points:
            return ()

        result: list[CenterlineDistancePoint] = [
            CenterlineDistancePoint(
                survey_index=0,
                distance_metres=0.0,
            )
        ]

        cumulative_distance = 0.0

        for index in range(1, len(points)):
            previous = points[index - 1]
            current = points[index]

            cumulative_distance += self._distance(
                latitude_1=previous.latitude,
                longitude_1=previous.longitude,
                latitude_2=current.latitude,
                longitude_2=current.longitude,
            )

            result.append(
                CenterlineDistancePoint(
                    survey_index=index,
                    distance_metres=cumulative_distance,
                )
            )

        return tuple(result)

    @staticmethod
    def _distance(
        latitude_1: float,
        longitude_1: float,
        latitude_2: float,
        longitude_2: float,
    ) -> float:
        """
        Calculate great-circle distance using
        the haversine formula.
        """

        lat_1 = radians(latitude_1)
        lat_2 = radians(latitude_2)

        delta_lat = radians(latitude_2 - latitude_1)
        delta_lon = radians(longitude_2 - longitude_1)

        a = (
            sin(delta_lat / 2.0) ** 2
            + cos(lat_1) * cos(lat_2) * sin(delta_lon / 2.0) ** 2
        )

        c = 2.0 * asin(sqrt(a))

        return EARTH_RADIUS_METRES * c
