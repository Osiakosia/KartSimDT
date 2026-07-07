"""
beacons.py

KartSimDT AIM Import Module

Parses AIM beacon marker information.
"""

from __future__ import annotations


class AimBeaconParser:
    """
    Parses AIM beacon marker information.
    """

    def parse(
        self,
        metadata: dict[str, str],
    ) -> list[float]:
        """
        Parse AIM beacon marker timestamps.

        Returns
        -------
        list[float]
            Lap end timestamps in seconds.
        """

        value = metadata.get("Beacon Markers", "")

        if not value:
            return []

        beacons: list[float] = []

        for item in value.split(";"):

            item = item.strip()

            if not item:
                continue

            item = item.replace(",", ".")

            beacons.append(float(item))

        return beacons
