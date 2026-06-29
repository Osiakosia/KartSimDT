"""
lap.py

KartSimDT Telemetry Module

Defines the Lap domain object representing one completed lap.

Version:
    v0.1

Status:
    Development
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Lap:
    """
    Represents one completed lap.

    The Lap object is independent of telemetry source formats
    such as AIM, MyChron or MoTeC.
    """

    number: int

    start_time: float
    end_time: float
    duration: float

    valid: bool = True

    sector1: float | None = None
    sector2: float | None = None
    sector3: float | None = None

    notes: str = ""

    @property
    def has_sectors(self) -> bool:
        """Return True if all sector times are available."""
        return (
            self.sector1 is not None
            and self.sector2 is not None
            and self.sector3 is not None
        )

    @property
    def total_sector_time(self) -> float | None:
        """Return total sector time."""
        if not self.has_sectors:
            return None

        assert (
            self.sector1 is not None
            and self.sector2 is not None
            and self.sector3 is not None
        )

        return self.sector1 + self.sector2 + self.sector3
