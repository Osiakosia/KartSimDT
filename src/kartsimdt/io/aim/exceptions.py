"""
exceptions.py

KartSimDT AIM Import Module

Custom exceptions used by the AIM import subsystem.
"""

from __future__ import annotations


class AimImportError(Exception):
    """
    Base exception for all AIM import errors.
    """


class InvalidAimFileError(AimImportError):
    """
    Raised when the input file is not a valid AIM telemetry file.
    """


class UnsupportedAimVersionError(AimImportError):
    """
    Raised when the AIM file version is not supported.
    """


class MissingChannelError(AimImportError):
    """
    Raised when a required telemetry channel is missing.
    """


class InvalidChannelError(AimImportError):
    """
    Raised when a telemetry channel contains invalid data.
    """


class MappingError(AimImportError):
    """
    Raised when telemetry data cannot be mapped into the
    KartSimDT telemetry domain model.
    """


class ValidationError(AimImportError):
    """
    Raised when telemetry validation fails.
    """
