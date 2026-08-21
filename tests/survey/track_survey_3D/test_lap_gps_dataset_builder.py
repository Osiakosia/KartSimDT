"""
test_lap_gps_dataset_builder.py

Tests for LapGpsDatasetBuilder.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey_3d.full_lap import FullLap
from kartsimdt.survey.track_survey_3d.lap_gps_dataset_builder import (
    LapGpsDatasetBuilder,
)
from kartsimdt.telemetry.channel import TelemetryChannel
from kartsimdt.telemetry.session import TelemetrySession


def create_session() -> TelemetrySession:
    session = TelemetrySession()

    session.channels.add(
        TelemetryChannel(
            name="time",
            unit="s",
            samples=[
                0.0,
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
            ],
        )
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_latitude",
            unit="deg",
            samples=[
                54.000,
                54.001,
                54.002,
                54.003,
                54.004,
                54.005,
            ],
        )
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_longitude",
            unit="deg",
            samples=[
                24.000,
                24.001,
                24.002,
                24.003,
                24.004,
                24.005,
            ],
        )
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_altitude",
            unit="m",
            samples=[
                170.0,
                171.0,
                172.0,
                173.0,
                174.0,
                175.0,
            ],
        )
    )

    return session


def test_build_lap_gps_dataset() -> None:
    session = create_session()

    lap = FullLap(
        session_index=3,
        lap_number=7,
        start_time=2.0,
        end_time=5.0,
    )

    builder = LapGpsDatasetBuilder()

    dataset = builder.build(
        session=session,
        lap=lap,
    )

    print()
    print("========== LAP GPS DATASET ==========")
    print(f"Lap number    : {lap.lap_number}")
    print(f"Session index : {lap.session_index}")
    print(f"Start time    : {lap.start_time}")
    print(f"End time      : {lap.end_time}")
    print(f"GPS samples   : {dataset.count()}")

    for index, sample in enumerate(dataset.samples):
        print(
            f"[{index}] "
            f"lon={sample.longitude:.6f} "
            f"lat={sample.latitude:.6f} "
            f"elevation={sample.elevation} "
            f"session={sample.session_index}"
        )

    print("=====================================")

    assert dataset.count() == 3

    assert dataset.samples[0].longitude == 24.002
    assert dataset.samples[0].latitude == 54.002
    assert dataset.samples[0].elevation == 172.0
    assert dataset.samples[0].session_index == 3

    assert dataset.samples[1].longitude == 24.003
    assert dataset.samples[1].latitude == 54.003
    assert dataset.samples[1].elevation == 173.0
    assert dataset.samples[1].session_index == 3

    assert dataset.samples[2].longitude == 24.004
    assert dataset.samples[2].latitude == 54.004
    assert dataset.samples[2].elevation == 174.0
    assert dataset.samples[2].session_index == 3
