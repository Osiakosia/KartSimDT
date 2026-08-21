"""
Blender track context adapter.

Resolves the active track configured in KartSimDT Blender preferences.
"""

from __future__ import annotations

from kartsimdt.track.context import TrackContext
from kartsimdt.track.resolver import TrackResolver


def resolve_active_track(
    project_root,
    track_name: str,
) -> TrackContext:
    """
    Resolve the active track from Blender configuration.
    """

    tracks_root = project_root / "data" / "tracks"

    resolver = TrackResolver(
        tracks_root=tracks_root,
    )

    return resolver.resolve(track_name)
