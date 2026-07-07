"""
metadata.py

Track Survey metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SurveyMetadata:
    """
    Metadata describing a track survey.
    """

    name: str
    description: str = ""
