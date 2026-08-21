"""
Track runtime context.

Defines the filesystem resources belonging to one track.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class TrackContext:
    """
    Runtime context for one KartSimDT track.

    The track directory is the root of all track-specific data.
    """

    name: str
    root: Path

    @property
    def google_earth_dir(self) -> Path:
        """Google Earth source data directory."""
        return self.root / "google_earth"

    @property
    def centerline_kml(self) -> Path:
        """Canonical Track Survey KML entry point."""
        return self.google_earth_dir / "centerline.kml"

    @property
    def centerline_json(self) -> Path:
        """Canonical local centerline geometry."""
        return self.root / "centerline.json"

    @property
    def aim_dir(self) -> Path:
        """AIM telemetry directory."""
        return self.root / "aim"

    @property
    def blender_dir(self) -> Path:
        """Blender scene directory."""
        return self.root / "blender"

    @property
    def design_dir(self) -> Path:
        """Track design data directory."""
        return self.root / "design"

    @property
    def track_design_yaml(self) -> Path:
        """Track design definition."""
        return self.design_dir / "track_design.yaml"

    @property
    def walkthrough_dir(self) -> Path:
        """Walkthrough data directory."""
        return self.root / "walkthrough"

    @property
    def final_dir(self) -> Path:
        """Final/generated track data directory."""
        return self.root / "final"
