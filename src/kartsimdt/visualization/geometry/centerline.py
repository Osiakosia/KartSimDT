"""
centerline.py

Centerline geometry domain model.
"""

from __future__ import annotations

from dataclasses import dataclass

from kartsimdt.visualization.geometry.point import LocalPoint


@dataclass(slots=True)
class CenterlineGeometry:
    """
    Represents the local centerline geometry of a track.
    """

    name: str

    points: list[LocalPoint]
