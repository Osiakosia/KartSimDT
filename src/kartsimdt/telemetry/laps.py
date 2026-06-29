"""
laps.py

KartSimDT Telemetry Module

Defines the LapCollection domain object representing
a collection of telemetry laps.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .lap import Lap

from collections.abc import Iterator


@dataclass(slots=True)
class LapCollection:
    """
    Represents a collection of telemetry laps.

    Provides convenient methods for working with laps
    while remaining independent of telemetry source formats.
    """

    laps: list[Lap] = field(default_factory=list)

    def add(self, lap: Lap) -> None:
        """Add a lap to the collection."""
        self.laps.append(lap)

    def clear(self) -> None:
        """Remove all laps."""
        self.laps.clear()

    def count(self) -> int:
        """Return the number of laps."""
        return len(self.laps)

    def valid(self) -> list[Lap]:
        """Return all valid laps."""
        return [lap for lap in self.laps if lap.valid]

    def invalid(self) -> list[Lap]:
        """Return all invalid laps."""
        return [lap for lap in self.laps if not lap.valid]

    def fastest(self) -> Lap | None:
        """Return the fastest valid lap."""
        valid_laps = self.valid()

        if not valid_laps:
            return None

        return min(valid_laps, key=lambda lap: lap.duration)

    def total_time(self) -> float:
        """Return the total duration of all laps."""
        return sum(lap.duration for lap in self.laps)

    def __len__(self) -> int:
        """Return the number of laps."""
        return len(self.laps)

    def __iter__(self) -> Iterator[Lap]:
        """Iterate over laps."""
        return iter(self.laps)

    def __getitem__(self, index: int) -> Lap:
        """Return lap by index."""
        return self.laps[index]

    def is_empty(self) -> bool:
        """Return True if the collection contains no laps."""
        return len(self.laps) == 0

    def first(self) -> Lap | None:
        """Return the first lap."""
        if self.is_empty():
            return None
        return self.laps[0]

    def last(self) -> Lap | None:
        """Return the last lap."""
        if self.is_empty():
            return None
        return self.laps[-1]
