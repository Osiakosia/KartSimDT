"""
centerline.py

Track centerline domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .point import Point


@dataclass(slots=True)
class Centerline:
    """
    Represents the surveyed track centerline.
    """

    points: list[Point] = field(default_factory=list)

    def count(self) -> int:
        """q

        Return the number of surveyed points.
        """
        return len(self.points)
