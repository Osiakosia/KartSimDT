"""
normalized_elevation_profile.py

Normalized elevation profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NormalizedElevationPoint:
    """
    One normalized centerline elevation point.
    """

    survey_index: int
    elevation: float


@dataclass(frozen=True, slots=True)
class NormalizedElevationProfile:
    """
    One lap elevation profile with vertical GPS offset removed.
    """

    session_index: int
    lap_number: int
    points: tuple[NormalizedElevationPoint, ...]

    def count(self) -> int:
        return len(self.points)
