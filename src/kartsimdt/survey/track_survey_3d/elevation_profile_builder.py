"""
elevation_profile_builder.py

Builds one combined elevation profile from
multiple normalized lap profiles.
"""

from __future__ import annotations

from collections import defaultdict
from statistics import median

from .elevation_profile import (
    ElevationProfile,
    ElevationProfilePoint,
)
from .normalized_elevation_profile import (
    NormalizedElevationProfile,
)


class ElevationProfileBuilder:
    """
    Combines normalized lap profiles using
    the median elevation at each survey point.
    """

    def build(
        self,
        profiles: list[NormalizedElevationProfile],
    ) -> ElevationProfile:
        if not profiles:
            raise ValueError("No normalized elevation profiles provided")

        measurements: dict[int, list[float]] = defaultdict(list)

        for profile in profiles:
            for point in profile.points:
                measurements[point.survey_index].append(point.elevation)

        points = tuple(
            ElevationProfilePoint(
                survey_index=survey_index,
                elevation=median(values),
                measurement_count=len(values),
            )
            for survey_index, values in sorted(measurements.items())
        )

        return ElevationProfile(
            points=points,
        )
