"""
metadata.py

KartSimDT AIM Import Module

Extracts session metadata from AIM telemetry files.
"""

from __future__ import annotations

from typing import Any

import pandas as pd


class AimMetadataExtractor:
    """
    Extracts session metadata from raw AIM telemetry data.

    This class does not create KartSimDT domain objects.
    It only extracts metadata into a plain dictionary.
    """

    def extract(self, dataframe: pd.DataFrame) -> dict[str, Any]:
        """
        Extract session metadata from an AIM telemetry table.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Raw AIM telemetry data.

        Returns
        -------
        dict[str, Any]
            Extracted session metadata.

        Raises
        ------
        NotImplementedError
            Metadata extraction is not implemented yet.
        """
        raise NotImplementedError
