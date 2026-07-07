"""
segment_times.py

KartSimDT AIM Import Module

Parses AIM lap timing information.
"""

from __future__ import annotations


class AimSegmentTimeParser:
    """
    Parses AIM lap timing information from AIM metadata.

    Converts AIM lap time strings into floating-point
    durations expressed in seconds.
    """

    def parse(
        self,
        metadata: dict[str, str],
    ) -> list[float]:
        """
        Parse AIM segment times.

        Parameters
        ----------
        metadata : dict[str, str]
            AIM session metadata.

        Returns
        -------
        list[float]
            Lap durations in seconds.
        """

        value = metadata.get("Segment Times", "")

        if not value:
            return []

        lap_times: list[float] = []

        for item in value.split(";"):

            item = item.strip()

            if not item:
                continue

            lap_times.append(
                self._parse_time(item),
            )

        return lap_times

    def _parse_time(
        self,
        value: str,
    ) -> float:
        """
        Convert an AIM lap time string into seconds.

        Parameters
        ----------
        value : str
            AIM lap time.

        Returns
        -------
        float
            Lap duration in seconds.
        """

        value = value.replace(",", ".")

        minutes, seconds = value.split(":")

        return int(minutes) * 60 + float(seconds)
