"""
test_reader.py

Unit tests for the Track Survey KML reader.
"""

from pathlib import Path

import pytest

from kartsimdt.survey.track_survey.raw import TrackSurveyRawData
from kartsimdt.survey.track_survey.reader import TrackSurveyKmlReader


def test_reader_reads_reference_kml() -> None:
    """
    Verify that the reference KML file is read successfully.
    """

    file_path = Path(
        "tests/data/aukstadvaris/survey/centerline.kml",
    )

    reader = TrackSurveyKmlReader()

    raw = reader.read(file_path)

    assert isinstance(raw, TrackSurveyRawData)

    assert raw.metadata["name"] == "Aukstadvaris su aukščiu.kml"

    assert len(raw.coordinates) == 677


def test_reader_reads_first_coordinate() -> None:
    """
    Verify that the first coordinate is read correctly.
    """

    reader = TrackSurveyKmlReader()

    raw = reader.read(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    longitude, latitude, elevation = raw.coordinates[0]

    assert longitude == pytest.approx(24.52727465787633)
    assert latitude == pytest.approx(54.58621599452091)
    assert elevation is None


def test_reader_reads_last_coordinate() -> None:
    """
    Verify that the last coordinate is read correctly.
    """

    reader = TrackSurveyKmlReader()

    raw = reader.read(
        Path("tests/data/aukstadvaris/survey/centerline.kml"),
    )

    longitude, latitude, elevation = raw.coordinates[-1]

    longitude, latitude, elevation = raw.coordinates[-1]

    assert longitude == pytest.approx(24.52727223452272)
    assert latitude == pytest.approx(54.58621113192066)
    assert elevation is None
