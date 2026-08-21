from pathlib import Path

import pytest

from kartsimdt.track import TrackResolver


def test_resolver_resolves_track() -> None:
    tracks_root = Path("data") / "tracks"

    resolver = TrackResolver(
        tracks_root=tracks_root,
    )

    context = resolver.resolve(
        "Aukštadvaris",
    )

    assert context.name == "Aukštadvaris"
    assert context.root == (tracks_root / "Aukštadvaris")


def test_resolver_rejects_unknown_track() -> None:
    resolver = TrackResolver(
        tracks_root=Path("data") / "tracks",
    )

    with pytest.raises(FileNotFoundError):
        resolver.resolve(
            "NonExistingTrack",
        )
