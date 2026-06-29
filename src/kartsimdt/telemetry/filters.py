"""
filters.py

KartSimDT Telemetry Module

Telemetry signal filtering framework.
"""

from __future__ import annotations

from .channel import TelemetryChannel


class TelemetryFilters:
    """
    Signal filtering utilities.
    """

    @staticmethod
    def moving_average(channel: TelemetryChannel) -> TelemetryChannel:
        raise NotImplementedError

    @staticmethod
    def low_pass(channel: TelemetryChannel) -> TelemetryChannel:
        raise NotImplementedError

    @staticmethod
    def median(channel: TelemetryChannel) -> TelemetryChannel:
        raise NotImplementedError