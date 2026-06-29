"""
validator.py

KartSimDT AIM Import Module

Validates AIM CSV telemetry data before parsing.
"""

from __future__ import annotations

import pandas as pd


class AimValidator:
    """
    Validates raw AIM telemetry data.

    Raises an exception if validation fails.
    """

    def validate(self, dataframe: pd.DataFrame) -> None:
        """
        Validate an AIM telemetry table.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Raw AIM telemetry data.

        Raises
        ------
        NotImplementedError
            Validation is not implemented yet.
        """
        raise NotImplementedError
