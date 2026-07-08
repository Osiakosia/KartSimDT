"""
test_mapper.py

Unit tests for BlenderCurveMapper.
"""

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.visualization.blender.mapper import BlenderCurveMapper


def test_mapper_creates_blender_curve() -> None:
    """
    Verify that the mapper creates a BlenderCurve.
    """

    parser = TrackSurveyParser()

    session = parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    mapper = BlenderCurveMapper()

    curve = mapper.map(session)

    assert curve.name == session.metadata.name
    assert curve.count() == session.centerline.count()


def test_mapper_maps_first_point() -> None:
    """
    Verify that the first point is mapped correctly.
    """

    parser = TrackSurveyParser()

    session = parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    mapper = BlenderCurveMapper()

    curve = mapper.map(session)

    assert curve.points[0] == (
        session.centerline.points[0].longitude,
        session.centerline.points[0].latitude,
        0.0,
    )


def test_mapper_maps_last_point() -> None:
    """
    Verify that the last point is mapped correctly.
    """

    parser = TrackSurveyParser()

    session = parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    mapper = BlenderCurveMapper()

    curve = mapper.map(session)

    assert curve.points[-1] == (
        session.centerline.points[-1].longitude,
        session.centerline.points[-1].latitude,
        0.0,
    )
