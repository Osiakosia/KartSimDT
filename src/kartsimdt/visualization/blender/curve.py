"""
curve.py

Blender curve domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BlenderCurve:
    """
    Represents a curve prepared for Blender export.
    """

    name: str

    points: list[
        tuple[
            float,  # x
            float,  # y
            float,  # z
        ]
    ] = field(default_factory=list)

    def count(self) -> int:
        """
        Return the number of curve points.
        """
        return len(self.points)
