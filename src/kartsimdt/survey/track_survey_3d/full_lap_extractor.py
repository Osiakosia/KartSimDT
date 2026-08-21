"""
full_lap_extractor.py

Extracts complete laps from telemetry sessions.
"""

from __future__ import annotations

from kartsimdt.telemetry.session import TelemetrySession

from .full_lap import FullLap


class FullLapExtractor:
    """
    Extracts complete laps defined by consecutive lap boundaries.
    """

    def extract(
        self,
        session: TelemetrySession,
        session_index: int,
    ) -> list[FullLap]:
        full_laps: list[FullLap] = []

        laps = list(session.laps)

        for lap in laps:
            if lap.start_time <= 0.0:
                continue

            full_laps.append(
                FullLap(
                    session_index=session_index,
                    lap_number=lap.number,
                    start_time=lap.start_time,
                    end_time=lap.end_time,
                )
            )

        return full_laps
