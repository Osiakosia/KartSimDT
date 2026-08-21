"""
test_elevation_profile_builder.py

Tests for ElevationProfileBuilder.
"""

from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey_3d.elevation_profile_builder import (
    ElevationProfileBuilder,
)
from kartsimdt.survey.track_survey_3d.normalized_elevation_profile import (
    NormalizedElevationPoint,
    NormalizedElevationProfile,
)


def make_profile(
    session_index: int,
    values: list[float],
) -> NormalizedElevationProfile:
    return NormalizedElevationProfile(
        session_index=session_index,
        lap_number=3,
        points=tuple(
            NormalizedElevationPoint(
                survey_index=index,
                elevation=elevation,
            )
            for index, elevation in enumerate(values)
        ),
    )


def test_build_elevation_profile() -> None:
    profiles = [
        make_profile(0, [-2.0, 0.0, 2.0]),
        make_profile(1, [-2.1, 0.1, 2.1]),
        make_profile(2, [-1.9, -0.1, 50.0]),
    ]

    builder = ElevationProfileBuilder()

    profile = builder.build(
        profiles,
    )

    assert profile.count() == 3

    assert profile.points[0].elevation == pytest.approx(-2.0)
    assert profile.points[1].elevation == pytest.approx(0.0)

    # 50 m outlier must not dominate the result.
    assert profile.points[2].elevation == pytest.approx(2.1)

    assert profile.points[0].measurement_count == 3
    assert profile.points[1].measurement_count == 3
    assert profile.points[2].measurement_count == 3
