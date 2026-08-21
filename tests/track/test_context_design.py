from pathlib import Path

from kartsimdt.track.design import TrackDesign
from kartsimdt.track.resolver import TrackResolver

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRACKS_ROOT = PROJECT_ROOT / "data" / "tracks"


def test_resolve_track_and_load_design() -> None:
    resolver = TrackResolver(TRACKS_ROOT)

    context = resolver.resolve("Aukštadvaris")
    design = TrackDesign.from_context(context)

    assert context.name == "Aukštadvaris"
    assert context.track_design_yaml.is_file()

    assert design.road.default_width_m == 8.0
    assert design.start_finish.centerline_index == 662
