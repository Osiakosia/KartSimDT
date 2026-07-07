"""
exceptions.py

Track Survey exceptions.
"""

from __future__ import annotations


class TrackSurveyError(Exception):
    """
    Base exception for the Track Survey module.
    """


class InvalidTrackSurveyError(TrackSurveyError):
    """
    Raised when a survey file is invalid or cannot be parsed.
    """
