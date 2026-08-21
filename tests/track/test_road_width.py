from pathlib import Path

from kartsimdt.track.design import TrackDesign
from kartsimdt.track.road_width import RoadWidthResolver

PROJECT_ROOT = Path(__file__).resolve().parents[2]

TRACK_DESIGN = (
    PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "design" / "track_design.yaml"
)


def test_default_road_width() -> None:
    design = TrackDesign.from_yaml(TRACK_DESIGN)
    resolver = RoadWidthResolver(design.road)

    assert resolver.width_for_index(100) == 8.0


def test_start_finish_width() -> None:
    design = TrackDesign.from_yaml(TRACK_DESIGN)
    resolver = RoadWidthResolver(design.road)

    assert resolver.width_for_index(640) == 11.0
    assert resolver.width_for_index(662) == 11.0
    assert resolver.width_for_index(676) == 11.0


def test_after_start_finish_returns_to_default() -> None:
    design = TrackDesign.from_yaml(TRACK_DESIGN)
    resolver = RoadWidthResolver(design.road)

    assert resolver.width_for_index(677) == 8.0
