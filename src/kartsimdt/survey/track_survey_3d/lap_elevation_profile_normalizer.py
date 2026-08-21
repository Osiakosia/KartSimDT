"""
lap_elevation_profile_normalizer.py

Normalizes lap elevation profiles by removing
their absolute vertical GPS offset.
"""

from __future__ import annotations

from statistics import mean

from .lap_elevation_profile import LapElevationProfile
from .normalized_elevation_profile import (
    NormalizedElevationPoint,
    NormalizedElevationProfile,
)


class LapElevationProfileNormalizer:
    """
    Removes the vertical offset from one lap elevation profile.

    The profile shape is preserved while its mean elevation
    is shifted to zero.
    """

    def normalize(
        self,
        profile: LapElevationProfile,
    ) -> NormalizedElevationProfile:
        matches = profile.matches.matches

        if not matches:
            raise ValueError("Lap elevation profile contains no points")

        elevations = [float(match.gps_sample.elevation) for match in matches]

        profile_mean = mean(elevations)

        points = tuple(
            NormalizedElevationPoint(
                survey_index=match.survey_index,
                elevation=(float(match.gps_sample.elevation) - profile_mean),
            )
            for match in matches
        )

        return NormalizedElevationProfile(
            session_index=profile.session_index,
            lap_number=profile.lap_number,
            points=points,
        )
