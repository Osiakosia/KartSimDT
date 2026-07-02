"""
test_channels.py

Unit tests for the AIM channel registry.
"""

from __future__ import annotations

from kartsimdt.io.aim.channels import AimChannelRegistry


def test_channel_registry_is_not_empty() -> None:
    """
    Verify that the AIM channel registry contains registered channels.
    """
    assert AimChannelRegistry.CHANNEL_MAP


def test_has_channel() -> None:
    """
    Verify that the registry correctly identifies
    supported and unsupported AIM channels.
    """
    assert AimChannelRegistry.has_channel("GPS Speed")
    assert AimChannelRegistry.has_channel("RPM")

    assert not AimChannelRegistry.has_channel("Unknown Channel")


def test_get_channel_name() -> None:
    """
    Verify that AIM channel names are correctly mapped
    to KartSimDT channel identifiers.
    """
    assert AimChannelRegistry.get_channel_name("GPS Speed") == "gps_speed"

    assert AimChannelRegistry.get_channel_name("GPS Latitude") == "gps_latitude"

    assert AimChannelRegistry.get_channel_name("RPM") == "engine_rpm"


def test_supported_channels() -> None:
    """
    Verify that the registry returns all supported
    AIM channel names.
    """
    channels = AimChannelRegistry.supported_channels()

    assert "Time" in channels
    assert "GPS Speed" in channels
    assert "GPS Latitude" in channels
    assert "GPS Longitude" in channels
    assert "RPM" in channels


def test_required_channels_exist() -> None:
    """
    Verify that all required AIM telemetry channels
    are registered.
    """
    required_channels = [
        "Time",
        "GPS Speed",
        "GPS Latitude",
        "GPS Longitude",
        "RPM",
    ]

    for channel in required_channels:
        assert AimChannelRegistry.has_channel(channel)
