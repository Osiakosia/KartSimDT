from pathlib import Path

from kartsimdt.track import TrackContext


def test_track_context_paths() -> None:
    root = Path("data") / "tracks" / "Aukštadvaris"

    context = TrackContext(
        name="Aukštadvaris",
        root=root,
    )

    assert context.name == "Aukštadvaris"
    assert context.root == root

    assert context.centerline_kml == root / "google_earth" / "centerline.kml"

    assert context.centerline_json == root / "centerline.json"
    assert context.aim_dir == root / "aim"
    assert context.blender_dir == root / "blender"
    assert context.walkthrough_dir == root / "walkthrough"
    assert context.final_dir == root / "final"
