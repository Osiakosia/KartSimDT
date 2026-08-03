"""
validator.py

KartSimDT Track Survey 3D Module

Validates Track Survey and canonical telemetry data
required for Track Survey 3D generation.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.telemetry.session import TelemetrySession

from .constants import REQUIRED_GPS_CHANNELS
from .exceptions import (
    InvalidTelemetry3DError,
    InvalidTrackSurvey3DError,
)


class TrackSurvey3DValidator:
    """
    Validate inputs required for Track Survey 3D generation.
    """

    def validate(
        self,
        survey: TrackSurveySession,
        telemetry_sessions: list[TelemetrySession],
    ) -> None:
        """
        Validate Track Survey and telemetry inputs.
        """

        self._validate_survey(survey)
        self._validate_telemetry_sessions(telemetry_sessions)

    def _validate_survey(
        self,
        survey: TrackSurveySession,
    ) -> None:
        """
        Validate the base Track Survey.
        """

        if not survey.centerline.points:
            raise InvalidTrackSurvey3DError(
                "Track Survey centerline contains no points."
            )

    def _validate_telemetry_sessions(
        self,
        telemetry_sessions: list[TelemetrySession],
    ) -> None:
        """
        Validate telemetry sessions used as elevation sources.
        """

        if not telemetry_sessions:
            raise InvalidTelemetry3DError(
                "No telemetry sessions provided for Track Survey 3D."
            )

        for index, session in enumerate(telemetry_sessions):
            self._validate_telemetry_session(
                session,
                index,
            )

    def _validate_telemetry_session(
        self,
        session: TelemetrySession,
        index: int,
    ) -> None:
        """
        Validate one telemetry session.
        """

        for channel_name in REQUIRED_GPS_CHANNELS:
            if not session.channels.exists(channel_name):
                raise InvalidTelemetry3DError(
                    f"Telemetry session {index} is missing "
                    f"required channel '{channel_name}'."
                )

            channel = session.channels.get(channel_name)

            if channel is None:
                raise InvalidTelemetry3DError(
                    f"Telemetry session {index} could not load "
                    f"required channel '{channel_name}'."
                )

            if channel.is_empty():
                raise InvalidTelemetry3DError(
                    f"Telemetry session {index} channel "
                    f"'{channel_name}' contains no samples."
                )

        self._validate_channel_lengths(
            session,
            index,
        )

    def _validate_channel_lengths(
        self,
        session: TelemetrySession,
        index: int,
    ) -> None:
        """
        Validate synchronization of required GPS channels.
        """

        sample_counts: dict[str, int] = {}

        for channel_name in REQUIRED_GPS_CHANNELS:
            channel = session.channels.get(channel_name)

            if channel is None:
                raise InvalidTelemetry3DError(
                    f"Telemetry session {index} could not load "
                    f"required channel '{channel_name}'."
                )

            sample_counts[channel_name] = channel.count()

        if len(set(sample_counts.values())) != 1:
            counts = ", ".join(
                f"{name}={count}" for name, count in sample_counts.items()
            )

            raise InvalidTelemetry3DError(
                f"Telemetry session {index} GPS channel "
                f"sample counts do not match: {counts}."
            )
