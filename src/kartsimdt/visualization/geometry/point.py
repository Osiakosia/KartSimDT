"""
point.py

Local 3D geometry point.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LocalPoint:
    """
    Represents one local 3D point.

    All coordinates are expressed in metres relative
    to the local track origin.
    """

    x: float
    y: float
    z: float
