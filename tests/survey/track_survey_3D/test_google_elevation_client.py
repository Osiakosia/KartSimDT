"""
Tests for Google Elevation API integration.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock, patch

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey_3d.google_elevation_client import (
    GoogleElevationClient,
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]

CENTERLINE_FILE = (
    PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
)


def test_centerline_contains_677_points() -> None:
    """Centerline KML must provide the expected 677 survey points."""

    survey = TrackSurveyParser().parse(
        CENTERLINE_FILE,
    )

    points = survey.centerline.points

    assert len(points) == 677

    assert points[0].latitude == 54.58621599429108
    assert points[0].longitude == 24.52727465787633

    assert points[-1].latitude is not None
    assert points[-1].longitude is not None


@patch("kartsimdt.survey.track_survey_3d.google_elevation_client.requests.get")
def test_google_elevation_client_returns_points(
    mock_get: Mock,
) -> None:
    """Google Elevation Client maps API response to domain points."""

    mock_response = Mock()

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "status": "OK",
        "results": [
            {
                "elevation": 147.9389343261719,
                "location": {
                    "lat": 54.586216,
                    "lng": 24.527275,
                },
                "resolution": 152.7032318115234,
            },
            {
                "elevation": 148.125,
                "location": {
                    "lat": 54.586227,
                    "lng": 24.527274,
                },
                "resolution": 152.7032318115234,
            },
        ],
    }

    mock_get.return_value = mock_response

    survey = TrackSurveyParser().parse(
        CENTERLINE_FILE,
    )

    points = survey.centerline.points[:2]

    client = GoogleElevationClient(
        api_key="test-api-key",
    )

    result = client.get_elevations(points)

    assert len(result) == 2

    assert result[0].elevation == 147.9389343261719
    assert result[0].latitude == 54.586216
    assert result[0].longitude == 24.527275
    assert result[0].resolution == 152.7032318115234

    assert result[1].elevation == 148.125

    mock_get.assert_called_once()

    request_params = mock_get.call_args.kwargs["params"]

    assert request_params["key"] == "test-api-key"
    assert request_params["locations"] == (
        "54.58621599429108,24.52727465787633" "|54.58622733617794,24.52727367335561"
    )


def test_google_elevation_client_empty_points() -> None:
    """Empty input must return an empty result."""

    client = GoogleElevationClient(
        api_key="test-api-key",
    )

    result = client.get_elevations([])

    assert result == []


@patch("kartsimdt.survey.track_survey_3d.google_elevation_client.requests.get")
def test_google_elevation_client_rejects_api_error(
    mock_get: Mock,
) -> None:
    """Google API errors must raise RuntimeError."""

    mock_response = Mock()

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "status": "REQUEST_DENIED",
        "error_message": "The provided API key is invalid.",
    }

    mock_get.return_value = mock_response

    survey = TrackSurveyParser().parse(
        CENTERLINE_FILE,
    )

    client = GoogleElevationClient(
        api_key="invalid-key",
    )

    points = survey.centerline.points[:1]

    try:
        client.get_elevations(points)
    except RuntimeError as exc:
        assert "REQUEST_DENIED" in str(exc)
    else:
        raise AssertionError("Expected RuntimeError for Google API error.")
