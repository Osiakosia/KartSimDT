"""
lap_gps_dataset_builder.py

Builds a GPS elevation dataset for a single complete telemetry lap.
"""

from __future__ import annotations

from kartsimdt.telemetry.session import TelemetrySession

from .full_lap import FullLap
from .gps_dataset import GpsElevationDataset
from .gps_sample import GpsElevationSample


class LapGpsDatasetBuilder:
    """
    Builds GPS elevation samples belonging to one complete lap.
    """

    def build(
        self,
        session: TelemetrySession,
        lap: FullLap,
    ) -> GpsElevationDataset:
        time_channel = session.channels.get("time")
        latitude_channel = session.channels.get("gps_latitude")
        longitude_channel = session.channels.get("gps_longitude")
        altitude_channel = session.channels.get("gps_altitude")

        if (
                time_channel is None
                or latitude_channel is None
                or longitude_channel is None
                or altitude_channel is None
        ):
            raise ValueError(
                "Telemetry session is missing required GPS channels."
            )

        dataset = GpsElevationDataset()

        for time, latitude, longitude, altitude in zip(
                time_channel.samples,
                latitude_channel.samples,
                longitude_channel.samples,
                altitude_channel.samples,
                strict=True,
        ):
            if time < lap.start_time:
                continue

            if time >= lap.end_time:
                break

            dataset.add(
                GpsElevationSample(
                    longitude=float(longitude),
                    latitude=float(latitude),
                    elevation=altitude,
                    session_index=lap.session_index,
                )
            )

        return dataset
