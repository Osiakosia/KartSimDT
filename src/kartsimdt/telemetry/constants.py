"""
constants.py

KartSimDT Telemetry Module

Shared constants used throughout the telemetry module.
"""

DEFAULT_SAMPLING_FREQUENCY = 50.0

DEFAULT_TIME_UNIT = "s"
DEFAULT_DISTANCE_UNIT = "m"
DEFAULT_SPEED_UNIT = "km/h"
DEFAULT_ACCELERATION_UNIT = "m/s²"
DEFAULT_RPM_UNIT = "rpm"

SUPPORTED_CHANNELS = (
    "Speed",
    "RPM",
    "Throttle",
    "Brake",
    "Steering",
    "GPS Latitude",
    "GPS Longitude",
    "Altitude",
    "Lateral G",
    "Longitudinal G",
)
