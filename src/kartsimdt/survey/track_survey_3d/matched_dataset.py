"""
matched_dataset.py

Track Survey 3D matched elevation dataset.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .matched_elevation import MatchedElevation


@dataclass(slots=True)
class MatchedElevationDataset:
    """
    Collection of matched Track Survey elevations.
    """

    matches: list[MatchedElevation] = field(default_factory=list)

    def add(
        self,
        match: MatchedElevation,
    ) -> None:
        """
        Add one matched elevation.
        """

        self.matches.append(match)

    def clear(self) -> None:
        """
        Remove all matches.
        """

        self.matches.clear()

    def count(self) -> int:
        """
        Return the number of matches.
        """

        return len(self.matches)

    def is_empty(self) -> bool:
        """
        Return True if no matches exist.
        """

        return len(self.matches) == 0
