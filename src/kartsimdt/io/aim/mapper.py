"""
mapper.py

KartSimDT AIM Import Module

Maps validated AIM raw data into the KartSimDT telemetry domain model.
"""

from __future__ import annotations

from kartsimdt.io.aim.beacons import AimBeaconParser
from kartsimdt.io.aim.segment_times import AimSegmentTimeParser

from ...telemetry.channel import TelemetryChannel
from ...telemetry.channels import ChannelCollection
from ...telemetry.lap import Lap
from ...telemetry.laps import LapCollection
from ...telemetry.metadata import SessionMetadata
from ...telemetry.session import TelemetrySession
from .channels import AimChannelRegistry
from .exceptions import InvalidAimFileError
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

    def _map_metadata(
        self,
        raw: AimRawData,
    ) -> SessionMetadata:
        """
        Map AIM metadata into SessionMetadata.
        """

        metadata = raw.metadata

        return SessionMetadata(
            session_name=metadata.get("Session", ""),
            track_name=metadata.get("Session", ""),
            driver_name=metadata.get("Racer", ""),
            vehicle_name=metadata.get("Vehicle", ""),
            logger_name=metadata.get("Logger", ""),
            notes=metadata.get("Comment", ""),
            extra_metadata=metadata,
        )

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

    def _map_laps(
        self,
        raw: AimRawData,
    ) -> LapCollection:
        """
        Map AIM lap information into a LapCollection.
        """

        beacon_parser = AimBeaconParser()
        segment_parser = AimSegmentTimeParser()

        beacons = beacon_parser.parse(raw.metadata)
        durations = segment_parser.parse(raw.metadata)

        if len(beacons) != len(durations):
            raise InvalidAimFileError(
                "Beacon marker count does not match segment count."
            )

        laps = LapCollection()

        start_time = 0.0

        for number, (end_time, duration) in enumerate(
            zip(beacons, durations, strict=True),
            start=1,
        ):
            lap = Lap(
                number=number,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
            )

            laps.add(lap)

            start_time = end_time

        return laps
