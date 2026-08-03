"""
gps_dataset.py

Track Survey 3D GPS elevation dataset.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .gps_sample import GpsElevationSample


@dataclass(slots=True)
class GpsElevationDataset:
    """
    Collection of GPS elevation samples extracted
    from one or more telemetry sessions.
    """

    samples: list[GpsElevationSample] = field(default_factory=list)

    def add(
        self,
        sample: GpsElevationSample,
    ) -> None:
        """
        Add one GPS sample.
        """

        self.samples.append(sample)

    def clear(self) -> None:
        """
        Remove all samples.
        """

        self.samples.clear()

    def count(self) -> int:
        """
        Return the number of samples.
        """

        return len(self.samples)

    def is_empty(self) -> bool:
        """
        Return True if no samples exist.
        """

        return len(self.samples) == 0
