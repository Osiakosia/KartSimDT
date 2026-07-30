"""
parser.py

Track Survey parser.
"""

from __future__ import annotations

from pathlib import Path

from .mapper import TrackSurveyMapper
from .reader import TrackSurveyKmlReader
from .session import TrackSurveySession
from .validator import TrackSurveyValidator


class TrackSurveyParser:
    """
    Parses a survey dataset into a TrackSurveySession.
    """

    def __init__(self) -> None:
        self._reader = TrackSurveyKmlReader()
        self._validator = TrackSurveyValidator()
        self._mapper = TrackSurveyMapper()

    def parse(
        self,
        path: Path,
    ) -> TrackSurveySession:
        """
        Parse a survey dataset.
        """

        raw = self._reader.read(path)

        self._validator.validate(raw)

        return self._mapper.map(raw)
