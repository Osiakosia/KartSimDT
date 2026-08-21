"""
lap_elevation_profile.py

Elevation profile for one complete telemetry lap.
"""

from __future__ import annotations

from dataclasses import dataclass

from .matched_dataset import MatchedElevationDataset


@dataclass(frozen=True)
class LapElevationProfile:
    """
    Matched elevation profile for one telemetry lap.
    """

    session_index: int
    lap_number: int
    matches: MatchedElevationDataset

    def count(self) -> int:
        """
        Return the number of matched centerline points.
        """

        return self.matches.count()
