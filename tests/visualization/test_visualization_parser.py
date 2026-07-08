"""
Unit tests for BlenderParser.
"""

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.visualization.blender.parser import BlenderParser


def test_parser_creates_blender_curve() -> None:
    """
    Verify that the parser creates a BlenderCurve.
    """

    survey_parser = TrackSurveyParser()

    session = survey_parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    parser = BlenderParser()

    curve = parser.parse(session)

    assert curve.name == session.metadata.name
    assert curve.count() == session.centerline.count()


def test_parser_maps_first_point() -> None:
    """
    Verify that the first point is parsed correctly.
    """

    survey_parser = TrackSurveyParser()

    session = survey_parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    parser = BlenderParser()

    curve = parser.parse(session)

    assert curve.points[0] == (
        session.centerline.points[0].longitude,
        session.centerline.points[0].latitude,
        0.0,
    )


def test_parser_maps_last_point() -> None:
    """
    Verify that the last point is parsed correctly.
    """

    survey_parser = TrackSurveyParser()

    session = survey_parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    parser = BlenderParser()

    curve = parser.parse(session)

    assert curve.points[-1] == (
        session.centerline.points[-1].longitude,
        session.centerline.points[-1].latitude,
        0.0,
    )
