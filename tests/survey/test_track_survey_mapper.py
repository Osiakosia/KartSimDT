"""
test_track_survey_mapper.py

Unit tests for the Track Survey mapper.
"""

from pathlib import Path

import pytest

from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import KmlReader
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey.validator import TrackSurveyValidator


@pytest.fixture
def survey_session() -> TrackSurveySession:
    """
    Create a TrackSurveySession from the reference KML dataset.
    """

    reader = KmlReader()
    validator = TrackSurveyValidator()
    mapper = TrackSurveyMapper()

    raw = reader.read(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    validator.validate(raw)

    return mapper.map(raw)


def test_mapper_creates_track_survey_session(
    survey_session: TrackSurveySession,
) -> None:
    """
    Verify that the mapper creates a TrackSurveySession.
    """

    assert isinstance(survey_session, TrackSurveySession)


def test_mapper_maps_metadata(
    survey_session: TrackSurveySession,
) -> None:
    """
    Verify that survey metadata is mapped.
    """

    assert survey_session.metadata.name == "Aukstadvaris su aukščiu.kml"


def test_mapper_maps_centerline(
    survey_session: TrackSurveySession,
) -> None:
    """
    Verify that the centerline is mapped.
    """

    assert survey_session.centerline.count() == 677


def test_mapper_maps_first_point(
    survey_session: TrackSurveySession,
) -> None:
    """
    Verify the first mapped point.
    """

    point = survey_session.centerline.points[0]

    assert point.longitude == pytest.approx(24.52727465787633)
    assert point.latitude == pytest.approx(54.58621599452091)
    assert point.elevation is None


def test_mapper_maps_last_point(
    survey_session: TrackSurveySession,
) -> None:
    """
    Verify the last mapped point.
    """

    point = survey_session.centerline.points[-1]

    assert point.longitude == pytest.approx(24.52727223452272)
    assert point.latitude == pytest.approx(54.58621113192066)
    assert point.elevation is None
