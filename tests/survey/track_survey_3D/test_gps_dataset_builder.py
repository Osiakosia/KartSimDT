"""
test_gps_dataset_builder.py

Tests for GpsDatasetBuilder.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey_3d.gps_dataset_builder import (
    GpsDatasetBuilder,
)
from kartsimdt.telemetry.channel import TelemetryChannel
from kartsimdt.telemetry.session import TelemetrySession


def create_session() -> TelemetrySession:
    session = TelemetrySession()

    session.channels.add(
        TelemetryChannel(
            name="gps_latitude",
            unit="deg",
            samples=[54.000, 54.100, 54.200],
        )
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_longitude",
            unit="deg",
            samples=[24.000, 24.100, 24.200],
        )
    )

    session.channels.add(
        TelemetryChannel(
            name="gps_altitude",
            unit="m",
            samples=[176.0, 177.0, 178.0],
        )
    )

    return session


def test_build_single_session() -> None:
    builder = GpsDatasetBuilder()

    dataset = builder.build(
        [
            create_session(),
        ]
    )

    assert dataset.count() == 3

    assert dataset.samples[0].latitude == 54.000
    assert dataset.samples[0].longitude == 24.000
    assert dataset.samples[0].elevation == 176.0

    assert dataset.samples[2].latitude == 54.200
    assert dataset.samples[2].longitude == 24.200
    assert dataset.samples[2].elevation == 178.0


def test_build_multiple_sessions() -> None:
    builder = GpsDatasetBuilder()

    dataset = builder.build(
        [
            create_session(),
            create_session(),
        ]
    )

    assert dataset.count() == 6


def test_preserves_sample_order() -> None:
    builder = GpsDatasetBuilder()

    dataset = builder.build(
        [
            create_session(),
        ]
    )

    elevations = [sample.elevation for sample in dataset.samples]

    assert elevations == [
        176.0,
        177.0,
        178.0,
    ]
