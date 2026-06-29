"""
session.py

KartSimDT Telemetry Module

Defines the TelemetrySession domain object representing
a complete telemetry recording session.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .channels import ChannelCollection
from .laps import LapCollection
from .metadata import SessionMetadata


@dataclass(slots=True)
class TelemetrySession:
    """
    Represents one complete telemetry session.

    A telemetry session consists of:

    - Session metadata
    - Telemetry channels
    - Lap collection
    """

    metadata: SessionMetadata = field(default_factory=SessionMetadata)

    channels: ChannelCollection = field(default_factory=ChannelCollection)

    laps: LapCollection = field(default_factory=LapCollection)

    def is_empty(self) -> bool:
        """Return True if the session contains no telemetry."""
        return self.channels.is_empty() and self.laps.count() == 0

    def clear(self) -> None:
        """Clear all telemetry data."""
        self.channels.clear()
        self.laps.clear()

    def lap_count(self) -> int:
        """Return number of laps."""
        return self.laps.count()

    def channel_count(self) -> int:
        """Return number of telemetry channels."""
        return self.channels.count()
