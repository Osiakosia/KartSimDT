"""
validator.py

KartSimDT AIM Import Module

Validates raw AIM telemetry data.
"""

from __future__ import annotations

from .constants import REQUIRED_CHANNELS
from .exceptions import InvalidAimFileError
from .raw import AimRawData


class AimValidator:
    """
    Validates raw AIM telemetry data.
    """

    def validate(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate raw AIM telemetry data.
        """

        self._validate_structure(raw)
        self._validate_required_channels(raw)
        self._validate_timestamps(raw)
        self._validate_missing_values(raw)
        self._validate_version(raw)

    def _validate_structure(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate basic CSV structure.
        """

        if not raw.metadata:
            raise InvalidAimFileError("Metadata block is empty.")

        if not raw.channel_names:
            raise InvalidAimFileError("Channel names are missing.")

        if not raw.channel_units:
            raise InvalidAimFileError("Channel units are missing.")

        if raw.samples.empty:
            raise InvalidAimFileError("Telemetry samples are missing.")

        if len(raw.channel_names) != len(raw.channel_units):
            raise InvalidAimFileError("Channel names and units count do not match.")

        if raw.samples.shape[1] != len(raw.channel_names):
            raise InvalidAimFileError(
                "Sample column count does not match channel count."
            )

    def _validate_required_channels(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate required telemetry channels.
        """

        for channel in REQUIRED_CHANNELS:

            if channel not in raw.channel_names:
                raise InvalidAimFileError(f"Required channel '{channel}' is missing.")

    def _validate_timestamps(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate timestamp integrity.
        """

        time_index = raw.channel_names.index("Time")

        time_values = raw.samples.iloc[:, time_index]

        first_timestamp = time_values.iloc[0]

        if abs(first_timestamp) > 1e-6:
            raise InvalidAimFileError("Time channel must start at zero.")

        if not time_values.is_monotonic_increasing:
            raise InvalidAimFileError("Time channel is not monotonically increasing.")

        if time_values.duplicated().any():
            raise InvalidAimFileError("Time channel contains duplicated timestamps.")

    def _validate_missing_values(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate missing metadata, channel names and samples.

        TODO:
            - Metadata required values
            - Empty channel names
            - Missing sample values
        """

        pass

    def _validate_version(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate AIM CSV format version.

        TODO:
            - Format field exists
            - Supported AIM version
        """

        pass
