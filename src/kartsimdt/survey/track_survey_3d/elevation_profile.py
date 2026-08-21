"""
elevation_profile.py

Combined centerline elevation profile.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ElevationProfilePoint:
    """
    One combined centerline elevation point.
    """

    survey_index: int
    elevation: float
    measurement_count: int


@dataclass(frozen=True, slots=True)
class ElevationProfile:
    """
    Combined relative centerline elevation profile.
    """

    points: tuple[ElevationProfilePoint, ...]

    def count(self) -> int:
        return len(self.points)
