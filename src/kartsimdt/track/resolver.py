"""
Track resolver.

Resolves a track name into its filesystem context.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.track.context import TrackContext


class TrackResolver:
    """
    Resolve track names from the data/tracks directory.
    """

    def __init__(
        self,
        tracks_root: Path,
    ) -> None:
        self._tracks_root = tracks_root

    def resolve(
        self,
        track_name: str,
    ) -> TrackContext:
        """
        Resolve one track by name.
        """

        track_root = self._tracks_root / track_name

        if not track_root.is_dir():
            raise FileNotFoundError(f"Track directory not found: {track_root}")

        return TrackContext(
            name=track_name,
            root=track_root,
        )
