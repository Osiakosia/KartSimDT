"""
mapper.py

KartSimDT AIM Import Module

Maps validated AIM raw data into the KartSimDT telemetry domain model.
"""

from __future__ import annotations

from ...telemetry.channel import TelemetryChannel
from ...telemetry.channels import ChannelCollection
from ...telemetry.laps import LapCollection
from ...telemetry.metadata import SessionMetadata
from ...telemetry.session import TelemetrySession
from .channels import AimChannelRegistry
from .raw import AimRawData


class AimMapper:
    """
    Maps validated AIM raw data into the KartSimDT telemetry domain model.
    """

    def map(self, raw: AimRawData) -> TelemetrySession:
        """
        Convert validated AIM raw data into a telemetry session.
        """
        return TelemetrySession(
            metadata=self._map_metadata(raw),
            channels=self._map_channels(raw),
            laps=self._map_laps(raw),
        )

    def _map_metadata(self, raw: AimRawData) -> SessionMetadata:
        """
        Map AIM metadata into SessionMetadata.
        """
        raise NotImplementedError

    def _map_channels(self, raw: AimRawData) -> ChannelCollection:
        """
        Map AIM telemetry channels into a ChannelCollection.
        """
        channels = ChannelCollection()

        for raw_name, raw_unit in zip(
            raw.channel_names,
            raw.channel_units,
            strict=True,
        ):
            if not AimChannelRegistry.has_channel(raw_name):
                continue

            channel_name = AimChannelRegistry.get_channel_name(raw_name)
            unit = AimChannelRegistry.get_unit(raw_unit)

            samples = raw.samples[raw_name].tolist()

            channel = TelemetryChannel(
                name=channel_name,
                unit=unit,
                samples=samples,
            )

            channels.add(channel)

        return channels

    def _map_laps(self, raw: AimRawData) -> LapCollection:
        """
        Map AIM lap information into a LapCollection.
        """
        raise NotImplementedError
