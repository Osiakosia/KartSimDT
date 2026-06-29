"""
mapper.py

KartSimDT AIM Import Module

Maps raw AIM telemetry data into the KartSimDT telemetry domain model.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from ...telemetry.session import TelemetrySession


class AimMapper:
    """
    Maps AIM telemetry data into the KartSimDT telemetry domain model.
    """

    def map(
        self,
        dataframe: pd.DataFrame,
        metadata: dict[str, Any],
        laps: list[dict[str, Any]],
    ) -> TelemetrySession:
        """
        Map AIM telemetry data into a TelemetrySession.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Raw AIM telemetry data.

        metadata : dict[str, Any]
            Extracted session metadata.

        laps : list[dict[str, Any]]
            Extracted lap information.

        Returns
        -------
        TelemetrySession
            Mapped telemetry session.

        Raises
        ------
        NotImplementedError
            Mapping is not implemented yet.
        """
        raise NotImplementedError
