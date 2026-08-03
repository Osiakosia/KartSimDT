"""
gps_dataset_builder.py

Builds a GPS elevation dataset from canonical telemetry sessions.
"""

from __future__ import annotations

from kartsimdt.telemetry.session import TelemetrySession

from .constants import (
    GPS_ALTITUDE_CHANNEL,
    GPS_LATITUDE_CHANNEL,
    GPS_LONGITUDE_CHANNEL,
)
from .gps_dataset import GpsElevationDataset
from .gps_sample import GpsElevationSample


class GpsDatasetBuilder:
    """
    Builds a GPS elevation dataset from one or more
    canonical telemetry sessions.
    """

    def build(
        self,
        telemetry_sessions: list[TelemetrySession],
    ) -> GpsElevationDataset:
        """
        Build a GPS elevation dataset.
        """

        dataset = GpsElevationDataset()

        for session_index, session in enumerate(
            telemetry_sessions,
        ):
            self._append_session(
                dataset,
                session,
                session_index,
            )

        return dataset

    def _append_session(
        self,
        dataset: GpsElevationDataset,
        session: TelemetrySession,
        session_index: int,
    ) -> None:
        """
        Append one telemetry session to the dataset.
        """

        latitude = session.channels[GPS_LATITUDE_CHANNEL].samples

        longitude = session.channels[GPS_LONGITUDE_CHANNEL].samples

        altitude = session.channels[GPS_ALTITUDE_CHANNEL].samples

        for lat, lon, elev in zip(
            latitude,
            longitude,
            altitude,
            strict=True,
        ):
            dataset.add(
                GpsElevationSample(
                    latitude=lat,
                    longitude=lon,
                    elevation=elev,
                    session_index=session_index,
                )
            )
