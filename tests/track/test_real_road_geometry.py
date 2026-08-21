import json
from pathlib import Path

import pytest

from kartsimdt.track.design import TrackDesign
from kartsimdt.track.road_geometry import (
    Point3D,
    RoadGeometryGenerator,
)
from kartsimdt.track.road_width import RoadWidthResolver

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CENTERLINE_FILE = (
    PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "track_survey_blender.json"
)

DESIGN_FILE = (
    PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "design" / "track_design.yaml"
)


def load_centerline() -> list[Point3D]:
    with CENTERLINE_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    return [
        Point3D(
            x=point["x"],
            y=point["y"],
            z=point["z"],
        )
        for point in data
    ]


def test_real_aukstadvaris_road_geometry() -> None:
    centerline = load_centerline()

    design = TrackDesign.from_yaml(DESIGN_FILE)

    resolver = RoadWidthResolver(design.road)

    generator = RoadGeometryGenerator(
        centerline=centerline,
        width_resolver=resolver,
    )

    mesh = generator.generate()

    assert len(centerline) == 677
    assert len(mesh.vertices) == 1354
    assert len(mesh.faces) == 677


def test_real_aukstadvaris_start_finish_width() -> None:
    centerline = load_centerline()

    design = TrackDesign.from_yaml(DESIGN_FILE)

    resolver = RoadWidthResolver(design.road)

    generator = RoadGeometryGenerator(
        centerline=centerline,
        width_resolver=resolver,
    )

    mesh = generator.generate()

    for index in (640, 662, 676):
        left = mesh.vertices[index * 2]
        right = mesh.vertices[index * 2 + 1]

        width = (
            (left.x - right.x) ** 2 + (left.y - right.y) ** 2 + (left.z - right.z) ** 2
        ) ** 0.5

        assert width == pytest.approx(11.0)
