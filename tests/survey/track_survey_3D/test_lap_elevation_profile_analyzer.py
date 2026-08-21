"""
test_lap_elevation_profile_analyzer.py

Tests for LapElevationProfileAnalyzer.
"""

from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey_3d.gps_sample import (
    GpsElevationSample,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile_analyzer import (
    LapElevationProfileAnalyzer,
)
from kartsimdt.survey.track_survey_3d.matched_dataset import (
    MatchedElevationDataset,
)
from kartsimdt.survey.track_survey_3d.matched_elevation import (
    MatchedElevation,
)


def test_analyze_lap_elevation_profile() -> None:
    matches = MatchedElevationDataset()

    elevations = [
        175.0,
        177.0,
        179.0,
    ]

    for survey_index, elevation in enumerate(elevations):
        gps_sample = GpsElevationSample(
            latitude=54.001,
            longitude=24.001,
            elevation=elevation,
            session_index=2,
        )

        match = MatchedElevation(
            survey_index=survey_index,
            survey_latitude=54.001,
            survey_longitude=24.001,
            gps_sample=gps_sample,
            distance_metres=1.0,
        )

        matches.add(match)

    profile = LapElevationProfile(
        session_index=2,
        lap_number=7,
        matches=matches,
    )

    analyzer = LapElevationProfileAnalyzer()

    stats = analyzer.analyze(
        profile,
    )

    print()
    print("========== LAP ELEVATION PROFILE STATS ==========")
    print(f"Session : {stats.session_index}")
    print(f"Lap     : {stats.lap_number}")
    print(f"Points  : {stats.point_count}")
    print(f"Min     : {stats.minimum_elevation:.3f} m")
    print(f"Max     : {stats.maximum_elevation:.3f} m")
    print(f"Mean    : {stats.mean_elevation:.3f} m")
    print("=================================================")

    assert stats.session_index == 2
    assert stats.lap_number == 7
    assert stats.point_count == 3

    assert stats.minimum_elevation == pytest.approx(175.0)
    assert stats.maximum_elevation == pytest.approx(179.0)
    assert stats.mean_elevation == pytest.approx(177.0)
