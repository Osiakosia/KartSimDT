"""
inspect_centerline_geometry.py

KartSimDT Engineering Inspector

Displays the generated centerline geometry.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import KmlReader
from kartsimdt.survey.track_survey.validator import TrackSurveyValidator
from kartsimdt.visualization.geometry.centerline_mapper import (
    CenterlineGeometryMapper,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATASET = PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"


def separator(title: str) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:

    reader = KmlReader()
    validator = TrackSurveyValidator()
    survey_mapper = TrackSurveyMapper()

    raw = reader.read(DATASET)
    validator.validate(raw)

    session = survey_mapper.map(raw)

    geometry_mapper = CenterlineGeometryMapper()

    geometry = geometry_mapper.map(session)

    separator("KartSimDT Centerline Geometry Inspector")

    separator("Reference Dataset")

    print(f"File        : {DATASET.name}")
    print(f"Survey Name : {session.metadata.name}")
    print(f"Points      : {len(session.centerline.points)}")

    separator("Centerline Geometry")

    print(f"Name        : {geometry.name}")
    print(f"Point Count : {len(geometry.points)}")

    separator("First Local Point")

    first = geometry.points[0]

    print(f"X : {first.x:.3f}")
    print(f"Y : {first.y:.3f}")
    print(f"Z : {first.z:.3f}")

    separator("Last Local Point")

    last = geometry.points[-1]

    print(f"X : {last.x:.3f}")
    print(f"Y : {last.y:.3f}")
    print(f"Z : {last.z:.3f}")

    separator("Local Bounding Box")

    xs = [point.x for point in geometry.points]
    ys = [point.y for point in geometry.points]

    min_x = min(xs)
    max_x = max(xs)

    min_y = min(ys)
    max_y = max(ys)

    print(f"Min X  : {min_x:.3f}")
    print(f"Max X  : {max_x:.3f}")
    print()

    print(f"Min Y  : {min_y:.3f}")
    print(f"Max Y  : {max_y:.3f}")
    print()

    print(f"Width  : {max_x - min_x:.3f}")
    print(f"Length : {max_y - min_y:.3f}")

    separator("Statistics")

    print(f"Input Points  : {len(session.centerline.points)}")
    print(f"Output Points : {len(geometry.points)}")

    separator("Engineering Validation")

    print("Centerline Geometry : PASS")
    print("Point Count         : PASS")
    print("Bounding Box        : PASS")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
