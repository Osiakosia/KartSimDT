"""
reader.py

KartSimDT AIM Import Module

Reads AIM CSV telemetry files and loads them into memory.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class AimCsvReader:
    """
    Reads AIM CSV telemetry files.

    This class is responsible only for loading CSV data.
    It performs no validation or domain mapping.
    """

    def read(self, file_path: Path) -> pd.DataFrame:
        """
        Read an AIM CSV file.

        Parameters
        ----------
        file_path : Path
            Path to the AIM CSV file.

        Returns
        -------
        pandas.DataFrame
            Raw telemetry table.
        """
        return pd.read_csv(file_path)
