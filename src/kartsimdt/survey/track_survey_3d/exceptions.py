"""
exceptions.py

KartSimDT Track Survey 3D Module

Domain exceptions for Track Survey 3D generation.
"""

from __future__ import annotations


class TrackSurvey3DError(Exception):
    """
    Base exception for Track Survey 3D errors.
    """


class InvalidTrackSurvey3DError(TrackSurvey3DError):
    """
    Raised when Track Survey data is invalid
    for 3D generation.
    """


class InvalidTelemetry3DError(TrackSurvey3DError):
    """
    Raised when telemetry data is invalid
    for Track Survey 3D generation.
    """
