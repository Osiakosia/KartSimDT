"""
test_lap_elevation_profile_normalizer.py

Tests for LapElevationProfileNormalizer.
"""

from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey_3d.gps_sample import (
    GpsElevationSample,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile_normalizer import (
    LapElevationProfileNormalizer,
)
from kartsimdt.survey.track_survey_3d.matched_dataset import (
    MatchedElevationDataset,
)
from kartsimdt.survey.track_survey_3d.matched_elevation import (
    MatchedElevation,
)


def test_normalize_lap_elevation_profile() -> None:
    matches = MatchedElevationDataset()

    elevations = [
        175.0,
        177.0,
        179.0,
    ]

    for survey_index, elevation in enumerate(elevations):
        matches.add(
            MatchedElevation(
                survey_index=survey_index,
                survey_latitude=54.0,
                survey_longitude=24.0,
                gps_sample=GpsElevationSample(
                    latitude=54.0,
                    longitude=24.0,
                    elevation=elevation,
                    session_index=2,
                ),
                distance_metres=1.0,
            )
        )

    profile = LapElevationProfile(
        session_index=2,
        lap_number=7,
        matches=matches,
    )

    normalizer = LapElevationProfileNormalizer()

    normalized = normalizer.normalize(
        profile,
    )

    assert normalized.session_index == 2
    assert normalized.lap_number == 7
    assert normalized.count() == 3

    values = [point.elevation for point in normalized.points]

    assert values == pytest.approx([-2.0, 0.0, 2.0])

    assert sum(values) / len(values) == pytest.approx(0.0)
