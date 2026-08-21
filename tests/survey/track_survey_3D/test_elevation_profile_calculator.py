from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey_3d.elevation_profile_calculator import (
    ElevationProfileCalculator,
)


def test_calculate_empty_centerline() -> None:
    centerline = Centerline()

    result = ElevationProfileCalculator().calculate(
        centerline,
    )

    assert result == []


def test_calculate_elevation_profile() -> None:
    centerline = Centerline(
        points=[
            Point(
                longitude=23.700000,
                latitude=54.500000,
                elevation=100.0,
            ),
            Point(
                longitude=23.700100,
                latitude=54.500000,
                elevation=101.0,
            ),
            Point(
                longitude=23.700200,
                latitude=54.500000,
                elevation=103.0,
            ),
        ]
    )

    result = ElevationProfileCalculator().calculate(
        centerline,
    )

    assert len(result) == 3

    assert result[0].distance_metres == pytest.approx(0.0)
    assert result[0].elevation == pytest.approx(100.0)
    assert result[0].delta_elevation == pytest.approx(0.0)
    assert result[0].grade_percent == pytest.approx(0.0)

    assert result[1].elevation == pytest.approx(101.0)
    assert result[1].delta_elevation == pytest.approx(1.0)
    assert result[1].distance_metres > 0.0

    assert result[2].elevation == pytest.approx(103.0)
    assert result[2].delta_elevation == pytest.approx(2.0)
    assert result[2].distance_metres > result[1].distance_metres


def test_calculate_rejects_missing_elevation() -> None:
    centerline = Centerline(
        points=[
            Point(
                longitude=23.700000,
                latitude=54.500000,
                elevation=None,
            ),
        ]
    )

    with pytest.raises(ValueError, match="elevation"):
        ElevationProfileCalculator().calculate(
            centerline,
        )
