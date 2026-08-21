"""
Track road width resolution.

Resolves the effective road width for a centerline segment
from track-specific design data.
"""

from __future__ import annotations

from kartsimdt.track.design import RoadDesign


class RoadWidthResolver:
    """Resolve road width for a centerline segment."""

    def __init__(self, design: RoadDesign) -> None:
        self._design = design

    def width_for_index(self, index: int) -> float:
        """Return the effective road width for a centerline index."""

        for zone in self._design.width_zones:
            if zone.start_index <= index <= zone.end_index:
                return zone.width_m

        return self._design.default_width_m
