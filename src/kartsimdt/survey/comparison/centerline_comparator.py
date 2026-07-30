"""
Centerline comparator.
"""

from __future__ import annotations

from math import sqrt

from kartsimdt.survey.comparison.comparison_result import (
    ComparisonResult,
)
from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)
from kartsimdt.visualization.geometry.point import (
    LocalPoint,
)


class CenterlineComparator:
    """
    Compare two centerlines.
    """

    def distance(
        self,
        first: LocalPoint,
        second: LocalPoint,
    ) -> float:
        """
        Calculate planar distance.
        """

        dx = first.x - second.x
        dy = first.y - second.y

        return sqrt(
            dx * dx + dy * dy,
        )

    def nearest_distance(
        self,
        point: LocalPoint,
        points: list[LocalPoint],
    ) -> float:
        """
        Distance to nearest point.
        """

        return min(
            self.distance(
                point,
                candidate,
            )
            for candidate in points
        )

    def compare(
        self,
        reference: CenterlineGeometry,
        candidate: CenterlineGeometry,
    ) -> ComparisonResult:
        """
        Compare two centerlines.
        """

        errors = [
            self.nearest_distance(
                point,
                candidate.points,
            )
            for point in reference.points
        ]

        mean_error = sum(errors) / len(errors)

        max_error = max(errors)

        rmse = (sum(error * error for error in errors) / len(errors)) ** 0.5

        return ComparisonResult(
            reference_points=len(reference.points),
            candidate_points=len(candidate.points),
            mean_error=mean_error,
            max_error=max_error,
            rmse=rmse,
        )
