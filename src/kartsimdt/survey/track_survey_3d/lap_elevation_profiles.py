"""
lap_elevation_profiles.py

Collection of telemetry lap elevation profiles.
"""

from __future__ import annotations

from collections.abc import Iterator

from .lap_elevation_profile import LapElevationProfile


class LapElevationProfileCollection:
    """
    Collection of matched lap elevation profiles.
    """

    def __init__(self) -> None:
        self._profiles: list[LapElevationProfile] = []

    def add(
        self,
        profile: LapElevationProfile,
    ) -> None:
        self._profiles.append(profile)

    def count(self) -> int:
        return len(self._profiles)

    def __iter__(self) -> Iterator[LapElevationProfile]:
        return iter(self._profiles)
