"""
test_track_survey_parser.py
"""

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser


def test_parser_creates_track_survey_session() -> None:
    """
    Verify that the parser creates a TrackSurveySession.
    """

    parser = TrackSurveyParser()

    session = parser.parse(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    assert session.metadata.name == "Aukstadvaris su aukščiu.kml"
    assert session.centerline.count() == 677
