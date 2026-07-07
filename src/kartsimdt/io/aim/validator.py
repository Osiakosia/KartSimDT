"""
validator.py

KartSimDT AIM Import Module

Validates raw AIM telemetry data.
"""

from __future__ import annotations

from .constants import REQUIRED_CHANNELS, SUPPORTED_AIM_FORMATS
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
        Validate missing metadata, channel names and sample values.
        """

        self._validate_missing_metadata(raw)
        self._validate_missing_channel_names(raw)
        self._validate_missing_sample_values(raw)

    def _validate_missing_metadata(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate metadata values.
        """

        if "Format" not in raw.metadata:
            raise InvalidAimFileError("Metadata field 'Format' is missing.")

        value = raw.metadata["Format"]

        if value is None:
            raise InvalidAimFileError("Metadata field 'Format' is missing.")

        if isinstance(value, str) and not value.strip():
            raise InvalidAimFileError("Metadata field 'Format' is empty.")

    def _validate_missing_channel_names(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate empty channel names.
        """

        for name in raw.channel_names:

            if not name.strip():
                raise InvalidAimFileError("Channel name cannot be empty.")

    def _validate_missing_sample_values(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate missing telemetry sample values.
        """

        if raw.samples.isnull().values.any():
            raise InvalidAimFileError("Telemetry samples contain missing values.")

    def _validate_version(
        self,
        raw: AimRawData,
    ) -> None:
        """
        Validate AIM CSV format version.
        """

        if "Format" not in raw.metadata:
            raise InvalidAimFileError("Metadata field 'Format' is missing.")

        format_name = raw.metadata["Format"]

        if format_name not in SUPPORTED_AIM_FORMATS:
            raise InvalidAimFileError(f"Unsupported AIM format: {format_name}")
