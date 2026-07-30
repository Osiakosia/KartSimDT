"""
Tests for CenterlineGeometryMapper.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import TrackSurveyKmlReader
from kartsimdt.survey.track_survey.validator import (
    TrackSurveyValidator,
)
from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)
from kartsimdt.visualization.geometry.centerline_mapper import (
    CenterlineGeometryMapper,
)

TEST_DATA = Path(__file__).resolve().parents[1] / "data" / "aukstadvaris" / "survey"

DATASET = TEST_DATA / "centerline.kml"


def load_session():
    """
    Load the reference TrackSurveySession.
    """

    reader = TrackSurveyKmlReader()
    validator = TrackSurveyValidator()
    mapper = TrackSurveyMapper()

    raw = reader.read(DATASET)

    validator.validate(raw)

    return mapper.map(raw)


def test_mapper_creates_centerline_geometry() -> None:

    session = load_session()

    mapper = CenterlineGeometryMapper()

    geometry = mapper.map(session)

    assert isinstance(
        geometry,
        CenterlineGeometry,
    )


def test_mapper_preserves_point_count() -> None:

    session = load_session()

    mapper = CenterlineGeometryMapper()

    geometry = mapper.map(session)

    assert len(geometry.points) == len(session.centerline.points)


def test_mapper_maps_first_point() -> None:

    session = load_session()

    mapper = CenterlineGeometryMapper()

    geometry = mapper.map(session)

    first = geometry.points[0]

    assert first.x == 0.0
    assert first.y == 0.0
    assert first.z == 0.0


def test_mapper_maps_last_point() -> None:

    session = load_session()

    mapper = CenterlineGeometryMapper()

    geometry = mapper.map(session)

    last = geometry.points[-1]

    assert isinstance(last.x, float)
    assert isinstance(last.y, float)
    assert isinstance(last.z, float)
