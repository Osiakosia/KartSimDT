"""
constants.py

KartSimDT Track Survey 3D Module

Canonical telemetry channel names required for
Track Survey 3D generation.
"""

from __future__ import annotations

GPS_LATITUDE_CHANNEL = "gps_latitude"

GPS_LONGITUDE_CHANNEL = "gps_longitude"

GPS_ALTITUDE_CHANNEL = "gps_altitude"


REQUIRED_GPS_CHANNELS = (
    GPS_LATITUDE_CHANNEL,
    GPS_LONGITUDE_CHANNEL,
    GPS_ALTITUDE_CHANNEL,
)
