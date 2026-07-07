"""
raw.py

Raw Track Survey data container.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TrackSurveyRawData:
    """
    Raw data read from a survey source before validation and mapping.
    """

    metadata: dict[str, str]

    coordinates: list[
        tuple[
            float,  # longitude
            float,  # latitude
            float | None,  # elevation
        ]
    ]
