"""
metadata.py

KartSimDT Telemetry Module

Defines the SessionMetadata domain object representing
descriptive information about a telemetry session.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SessionMetadata:
    """
    Represents descriptive information about a telemetry session.

    This object contains session-level information only and is
    independent of the telemetry source format.
    """

    session_name: str = ""

    track_name: str = ""

    driver_name: str = ""

    vehicle_name: str = ""

    logger_name: str = ""

    recording_date: datetime | None = None

    sampling_frequency: float = 0.0

    notes: str = ""

    @property
    def has_driver(self) -> bool:
        """Return True if driver information is available."""
        return bool(self.driver_name)

    @property
    def has_track(self) -> bool:
        """Return True if track information is available."""
        return bool(self.track_name)

    @property
    def has_vehicle(self) -> bool:
        """Return True if vehicle information is available."""
        return bool(self.vehicle_name)

    @property
    def has_recording_date(self) -> bool:
        """Return True if recording date is available."""
        return self.recording_date is not None
