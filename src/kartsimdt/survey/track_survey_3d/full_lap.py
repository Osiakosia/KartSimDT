"""
full_lap.py

Represents a complete telemetry lap.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FullLap:
    session_index: int
    lap_number: int
    start_time: float
    end_time: float

    @property
    def duration(self) -> float:
        return self.end_time - self.start_time
