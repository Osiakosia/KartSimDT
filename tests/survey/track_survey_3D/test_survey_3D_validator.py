"""
test_validator.py

Tests for Track Survey 3D validator.
"""

from __future__ import annotations

import pytest

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.metadata import SurveyMetadata
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.exceptions import (
    InvalidTelemetry3DError,
    InvalidTrackSurvey3DError,
)
from kartsimdt.survey.track_survey_3d.validator import (
    TrackSurvey3DValidator,
)
from kartsimdt.telemetry.channel import TelemetryChannel
from kartsimdt.telemetry.session import TelemetrySession


def create_track_survey() -> TrackSurveySession:
    return TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(24.0, 54.0),
                Point(24.1, 54.1),
            ],
        ),
    )


def create_telemetry_session() -> TelemetrySession:
    session = TelemetrySession()

    session.channels.add(
        TelemetryChannel(
            name="gps_latitude",
            unit="deg",
            samples=[54.0, 54.1],
        ),
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_longitude",
            unit="deg",
            samples=[24.0, 24.1],
        ),
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_altitude",
            unit="m",
            samples=[176.0, 176.2],
        ),
    )

    return session


def test_valid_track_survey_3d() -> None:
    validator = TrackSurvey3DValidator()

    validator.validate(
        create_track_survey(),
        [
            create_telemetry_session(),
        ],
    )


def test_empty_centerline() -> None:
    validator = TrackSurvey3DValidator()

    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test",
            description="",
        ),
        centerline=Centerline(),
    )

    with pytest.raises(
        InvalidTrackSurvey3DError,
    ):
        validator.validate(
            survey,
            [
                create_telemetry_session(),
            ],
        )


def test_empty_telemetry_sessions() -> None:
    validator = TrackSurvey3DValidator()

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [],
        )


def test_missing_gps_latitude() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels.remove("gps_latitude")

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_missing_gps_longitude() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels.remove("gps_longitude")

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_missing_gps_altitude() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels.remove("gps_altitude")

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_empty_gps_latitude_samples() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels["gps_latitude"].clear()

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_empty_gps_longitude_samples() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels["gps_longitude"].clear()

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_empty_gps_altitude_samples() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels["gps_altitude"].clear()

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_different_channel_lengths() -> None:
    validator = TrackSurvey3DValidator()

    session = create_telemetry_session()

    session.channels["gps_altitude"].samples.pop()

    with pytest.raises(
        InvalidTelemetry3DError,
    ):
        validator.validate(
            create_track_survey(),
            [session],
        )


def test_multiple_valid_sessions() -> None:
    validator = TrackSurvey3DValidator()

    validator.validate(
        create_track_survey(),
        [
            create_telemetry_session(),
            create_telemetry_session(),
            create_telemetry_session(),
        ],
    )
