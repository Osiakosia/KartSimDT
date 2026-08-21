from pathlib import Path

from kartsimdt.track.design import TrackDesign

PROJECT_ROOT = Path(__file__).resolve().parents[2]

TRACK_DESIGN = (
    PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "design" / "track_design.yaml"
)


def test_load_aukstadvaris_track_design() -> None:
    design = TrackDesign.from_yaml(TRACK_DESIGN)

    assert design.road.default_width_m == 8.0

    assert len(design.road.width_zones) == 1

    zone = design.road.width_zones[0]

    assert zone.name == "start_finish"
    assert zone.start_index == 640
    assert zone.end_index == 676
    assert zone.width_m == 11.0

    assert design.start_finish.centerline_index == 662
    assert design.start_finish.straight_start_index == 640
    assert design.start_finish.straight_end_index == 676
    assert design.start_finish.straight_length_m == 105.36
