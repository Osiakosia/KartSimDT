"""
test_lap_elevation_profile.py

Tests for LapElevationProfile.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.matched_dataset import (
    MatchedElevationDataset,
)


def test_lap_elevation_profile() -> None:
    matches = MatchedElevationDataset()

    profile = LapElevationProfile(
        session_index=2,
        lap_number=7,
        matches=matches,
    )

    assert profile.session_index == 2
    assert profile.lap_number == 7
    assert profile.matches is matches
    assert profile.count() == 0
