"""
gps_sample.py

Track Survey 3D GPS elevation sample.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class GpsElevationSample:
    """
    One GPS measurement used for Track Survey 3D.
    """

    latitude: float
    longitude: float
    elevation: float
