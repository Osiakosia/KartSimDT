"""
test_centerline_distance_calculator.py

Tests for CenterlineDistanceCalculator.
"""

from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.metadata import SurveyMetadata
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.centerline_distance_calculator import (
    CenterlineDistanceCalculator,
)


def test_calculate_centerline_distances() -> None:
    centerline = Centerline(
        points=[
            Point(
                longitude=24.0000,
                latitude=54.0000,
            ),
            Point(
                longitude=24.0010,
                latitude=54.0000,
            ),
            Point(
                longitude=24.0020,
                latitude=54.0000,
            ),
        ]
    )

    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
        ),
        centerline=centerline,
    )

    calculator = CenterlineDistanceCalculator()

    distances = calculator.calculate(
        survey,
    )

    print()
    print("========== CENTERLINE DISTANCES ==========")

    for point in distances:
        print(f"Index {point.survey_index:2d} : " f"{point.distance_metres:8.3f} m")

    print("==========================================")

    assert len(distances) == 3

    assert distances[0].survey_index == 0
    assert distances[0].distance_metres == pytest.approx(0.0)

    assert distances[1].survey_index == 1
    assert distances[1].distance_metres > 0.0

    assert distances[2].survey_index == 2
    assert distances[2].distance_metres > distances[1].distance_metres

    assert distances[2].distance_metres == pytest.approx(
        distances[1].distance_metres * 2.0,
        rel=0.001,
    )
