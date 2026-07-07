"""
session.py

Track Survey session domain model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .centerline import Centerline
from .metadata import SurveyMetadata


@dataclass(slots=True)
class TrackSurveySession:
    """
    Represents one complete track survey.
    """

    metadata: SurveyMetadata
    centerline: Centerline
