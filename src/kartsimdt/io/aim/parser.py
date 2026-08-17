"""
parser.py

KartSimDT AIM Import Module

Main parser for AIM telemetry files.
"""

from __future__ import annotations

from pathlib import Path

from ...telemetry.session import TelemetrySession
from .mapper import AimMapper
from .reader import AimCsvReader
from .validator import AimValidator


class AimTelemetryParser:
    """
    Main entry point for AIM telemetry import.
    """

    def __init__(self) -> None:
        self._reader = AimCsvReader()
        self._validator = AimValidator()
        self._mapper = AimMapper()

    def parse(
        self,
        file_path: Path,
    ) -> TelemetrySession:
        """
        Parse an AIM telemetry file into a telemetry session.
        """

        raw = self._reader.read(
            file_path,
        )

        self._validator.validate(
            raw,
        )

        return self._mapper.map(
            raw,
        )
