"""
lap_selection_policy.py
"""

from __future__ import annotations

from .full_lap import FullLap

SKIP_INITIAL_FULL_LAPS = 1
LAPS_PER_SESSION = 9


class LapSelectionPolicy:
    """
    Select telemetry laps for elevation analysis.
    """

    def select(
        self,
        laps: list[FullLap],
    ) -> list[FullLap]:
        return laps[SKIP_INITIAL_FULL_LAPS : SKIP_INITIAL_FULL_LAPS + LAPS_PER_SESSION]
