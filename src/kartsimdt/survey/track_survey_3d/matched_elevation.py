"""
matched_elevation.py

Track Survey 3D matched elevation model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .gps_sample import GpsElevationSample


@dataclass(slots=True)
class MatchedElevation:
    """
    Represents one matched Track Survey point and
    its corresponding GPS elevation sample.
    """

    survey_index: int

    survey_latitude: float

    survey_longitude: float

    gps_sample: GpsElevationSample

    distance_metres: float
