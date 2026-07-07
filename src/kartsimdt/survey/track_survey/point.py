"""
point.py

Track Survey point domain model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    """
    Represents one surveyed point.
    """

    longitude: float
    latitude: float
    elevation: float | None = None
