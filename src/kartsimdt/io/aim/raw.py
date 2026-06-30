"""
raw.py

KartSimDT AIM Import Module

Raw AIM data structures.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True)
class AimRawData:
    """
    Raw data extracted from an AIM CSV file before conversion
    into the telemetry domain model.
    """

    metadata: dict[str, str]

    channel_names: list[str]

    channel_units: list[str]

    samples: pd.DataFrame
