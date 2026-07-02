"""
channels.py

KartSimDT AIM Import Module

Channel registry for AIM telemetry.
"""

from __future__ import annotations


class AimChannelRegistry:
    """
    Registry of supported AIM telemetry channels.
    """

    CHANNEL_MAP: dict[str, str] = {
        # Time
        "Time": "time",
        # GPS
        "GPS Speed": "gps_speed",
        "GPS Nsat": "gps_satellites",
        "GPS LatAcc": "gps_lateral_acceleration",
        "GPS LonAcc": "gps_longitudinal_acceleration",
        "GPS Slope": "gps_slope",
        "GPS Heading": "gps_heading",
        "GPS Gyro": "gps_gyro",
        "GPS Altitude": "gps_altitude",
        "GPS PosAccuracy": "gps_position_accuracy",
        "GPS SpdAccuracy": "gps_speed_accuracy",
        "GPS Radius": "gps_radius",
        "GPS Latitude": "gps_latitude",
        "GPS Longitude": "gps_longitude",
        # Logger
        "Logger Temperature": "logger_temperature",
        "Internal Batt": "internal_battery_voltage",
        # Engine
        "RPM": "engine_rpm",
        # Distance
        "Distance on GPS Speed": "distance",
    }

    UNIT_MAP: dict[str, str] = {
        # Time
        "s": "s",
        # Speed
        "km/h": "km/h",
        # Acceleration
        "g": "g",
        # Angle
        "deg": "deg",
        "deg/s": "deg/s",
        # Distance
        "m": "m",
        "mm": "mm",
        # Temperature
        "C": "°C",
        # Voltage
        "V": "V",
        # Engine
        "rpm": "rpm",
    }

    @classmethod
    def has_channel(cls, channel_name: str) -> bool:
        """
        Check whether a channel is supported.
        """
        return channel_name in cls.CHANNEL_MAP

    @classmethod
    def get_channel_name(cls, channel_name: str) -> str:
        """
        Return the normalized KartSimDT channel name.
        """
        return cls.CHANNEL_MAP[channel_name]

    @classmethod
    def get_unit(cls, unit: str) -> str:
        """
        Return normalized unit.
        """
        return cls.UNIT_MAP.get(unit, unit)

    @classmethod
    def supported_channels(cls) -> list[str]:
        """
        Return supported AIM channel names.
        """
        return list(cls.CHANNEL_MAP.keys())
