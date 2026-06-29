"""
channel.py

KartSimDT Telemetry Module

Defines the TelemetryChannel domain object representing
a single telemetry data channel.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TelemetryChannel:
    """
    Represents a single telemetry channel.

    Examples
    --------
    Speed
    RPM
    Throttle
    Brake
    GPS Latitude
    GPS Longitude
    Lateral G
    Longitudinal G
    """

    name: str
    unit: str

    samples: list[float] = field(default_factory=list)

    frequency: float = 0.0

    description: str = ""

    def add_sample(self, value: float) -> None:
        """Add one sample."""
        self.samples.append(value)

    def clear(self) -> None:
        """Remove all samples."""
        self.samples.clear()

    def count(self) -> int:
        """Return number of samples."""
        return len(self.samples)

    def is_empty(self) -> bool:
        """Return True if no samples exist."""
        return len(self.samples) == 0

    def minimum(self) -> float | None:
        """Return minimum sample value."""
        if self.is_empty():
            return None

        return min(self.samples)

    def maximum(self) -> float | None:
        """Return maximum sample value."""
        if self.is_empty():
            return None

        return max(self.samples)

    def average(self) -> float | None:
        """Return average sample value."""
        if self.is_empty():
            return None

        return sum(self.samples) / len(self.samples)

    def first(self) -> float | None:
        """Return first sample."""
        if self.is_empty():
            return None

        return self.samples[0]

    def last(self) -> float | None:
        """Return last sample."""
        if self.is_empty():
            return None

        return self.samples[-1]
