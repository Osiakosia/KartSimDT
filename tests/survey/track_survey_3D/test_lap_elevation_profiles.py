"""
test_lap_elevation_profiles.py

Tests for LapElevationProfileCollection.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profiles import (
    LapElevationProfileCollection,
)
from kartsimdt.survey.track_survey_3d.matched_dataset import (
    MatchedElevationDataset,
)


def test_add_profiles() -> None:
    profiles = LapElevationProfileCollection()

    first = LapElevationProfile(
        session_index=0,
        lap_number=3,
        matches=MatchedElevationDataset(),
    )

    second = LapElevationProfile(
        session_index=1,
        lap_number=4,
        matches=MatchedElevationDataset(),
    )

    profiles.add(first)
    profiles.add(second)

    result = list(profiles)

    assert profiles.count() == 2
    assert result[0] is first
    assert result[1] is second
