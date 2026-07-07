"""
test_mapper.py

Unit tests for the AIM mapper.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.channels import AimChannelRegistry
from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.raw import AimRawData
from kartsimdt.io.aim.reader import AimCsvReader


def test_map_channels_creates_all_supported_channels() -> None:
    """
    Verify that all supported AIM channels are mapped into
    a ChannelCollection.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    channels = mapper._map_channels(raw)

    assert not channels.is_empty()

    assert channels.count() == len(AimChannelRegistry.CHANNEL_MAP)

    assert channels.exists("time")
    assert channels.exists("gps_speed")
    assert channels.exists("gps_latitude")
    assert channels.exists("gps_longitude")
    assert channels.exists("engine_rpm")
    assert channels.exists("logger_temperature")
    assert channels.exists("distance")


def test_map_channels_copies_samples() -> None:
    """
    Verify that telemetry samples are copied into TelemetryChannel objects.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    channels = mapper._map_channels(raw)

    speed = channels["gps_speed"]

    assert speed.count() == len(raw.samples)

    assert speed.first() == raw.samples["GPS Speed"].iloc[0]
    assert speed.last() == raw.samples["GPS Speed"].iloc[-1]


def test_map_channels_normalizes_channel_names() -> None:
    """
    Verify that AIM channel names are normalized.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    channels = mapper._map_channels(raw)

    assert channels.exists("time")
    assert channels.exists("gps_speed")
    assert channels.exists("gps_satellites")
    assert channels.exists("gps_latitude")
    assert channels.exists("gps_longitude")
    assert channels.exists("engine_rpm")
    assert channels.exists("logger_temperature")
    assert channels.exists("distance")


def test_map_channels_normalizes_units() -> None:
    """
    Verify that channel units are normalized.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    channels = mapper._map_channels(raw)

    assert channels["time"].unit == "s"
    assert channels["gps_speed"].unit == "km/h"
    assert channels["gps_heading"].unit == "deg"
    assert channels["logger_temperature"].unit == "°C"
    assert channels["engine_rpm"].unit == "rpm"
    assert channels["distance"].unit == "m"


# ---------------------------------------------------------------------
# Lap mapping
# ---------------------------------------------------------------------


def test_map_laps_creates_lap_collection(
    validated_session: AimRawData,
) -> None:
    """
    Verify that AIM lap timing information is mapped into
    a LapCollection.
    """

    mapper = AimMapper()

    laps = mapper._map_laps(validated_session)

    assert not laps.is_empty()
    assert laps.count() == 15


def test_map_laps_maps_first_lap(
    validated_session: AimRawData,
) -> None:
    """
    Verify that the first lap is mapped correctly.
    """

    mapper = AimMapper()

    laps = mapper._map_laps(validated_session)

    lap = laps.first()

    assert lap is not None

    assert lap.number == 1
    assert lap.start_time == 0.0
    assert lap.end_time == 127.217
    assert lap.duration == 127.217


def test_map_laps_maps_last_lap(
    validated_session: AimRawData,
) -> None:
    """
    Verify that the last lap is mapped correctly.
    """

    mapper = AimMapper()

    laps = mapper._map_laps(validated_session)

    lap = laps.last()

    assert lap is not None

    assert lap.number == 15
    assert lap.duration == 101.350
    assert lap.end_time == 1042.990


def test_mapper_creates_telemetry_session(
    validated_session: AimRawData,
) -> None:
    """
    Verify that AimMapper creates a complete TelemetrySession.
    """

    mapper = AimMapper()

    session = mapper.map(validated_session)

    assert session.metadata is not None
    assert session.channels is not None
    assert session.laps is not None

    assert session.channels.count() == len(AimChannelRegistry.CHANNEL_MAP)

    assert session.laps.count() == 15
