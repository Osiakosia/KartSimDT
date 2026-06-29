"""
analysis.py

KartSimDT Telemetry Module

Telemetry analysis framework.
"""

from __future__ import annotations

from .session import TelemetrySession


class TelemetryAnalysis:
    """
    Performs telemetry analysis on a TelemetrySession.
    """

    def __init__(self, session: TelemetrySession):
        self.session = session
