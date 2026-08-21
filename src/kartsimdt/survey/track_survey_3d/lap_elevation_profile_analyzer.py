"""
lap_elevation_profile_analyzer.py

Statistical analysis of lap elevation profiles.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from .lap_elevation_profile import LapElevationProfile


@dataclass(frozen=True)
class LapElevationProfileStats:
    """
    Basic elevation statistics for one lap profile.
    """

    session_index: int
    lap_number: int
    point_count: int
    minimum_elevation: float
    maximum_elevation: float
    mean_elevation: float


class LapElevationProfileAnalyzer:
    """
    Calculates basic statistics for a lap elevation profile.
    """

    def analyze(
        self,
        profile: LapElevationProfile,
    ) -> LapElevationProfileStats:
        elevations = [
            float(match.gps_sample.elevation) for match in profile.matches.matches
        ]

        if not elevations:
            raise ValueError("Lap elevation profile contains no points")

        return LapElevationProfileStats(
            session_index=profile.session_index,
            lap_number=profile.lap_number,
            point_count=len(elevations),
            minimum_elevation=min(elevations),
            maximum_elevation=max(elevations),
            mean_elevation=mean(elevations),
        )
