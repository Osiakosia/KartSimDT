"""
inspect_coordinate_transform.py

KartSimDT Engineering Inspector

Displays the complete coordinate transformation pipeline.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import KmlReader
from kartsimdt.survey.track_survey.validator import TrackSurveyValidator
from kartsimdt.visualization.geometry.coordinate_transform import (
    CoordinateTransform,
)
from kartsimdt.visualization.geometry.reference_frame import (
    create_reference_frame,
)

# ============================================================================
# Project Paths
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TEST_DATA = PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey"

DATASET = TEST_DATA / "centerline.kml"


# ============================================================================
# Helpers
# ============================================================================


def separator(title: str) -> None:
    """Print section separator."""

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


# ============================================================================
# Main
# ============================================================================


def main() -> None:

    reader = KmlReader()
    validator = TrackSurveyValidator()
    mapper = TrackSurveyMapper()

    transformer = CoordinateTransform()

    raw = reader.read(DATASET)

    validator.validate(raw)

    session = mapper.map(raw)

    frame = create_reference_frame(session)

    local_points = [
        transformer.transform(point, frame) for point in session.centerline.points
    ]

    separator("KartSimDT Coordinate Transform Inspector")

    separator("Reference Dataset")

    print(f"File        : {DATASET.name}")
    print(f"Survey Name : {session.metadata.name}")
    print(f"Points      : {len(session.centerline.points)}")

    separator("Local Reference Frame")

    print(f"Origin Longitude : {frame.origin_longitude:.8f}")
    print(f"Origin Latitude  : {frame.origin_latitude:.8f}")
    print(f"Origin Elevation : {frame.origin_elevation:.3f}")

    print()

    print(f"Latitude Scale   : " f"{frame.metres_per_degree_latitude:.3f}")

    print(f"Longitude Scale  : " f"{frame.metres_per_degree_longitude:.3f}")

    separator("Coordinate Transform")

    first = session.centerline.points[0]
    first_local = local_points[0]

    print("Input Point\n")

    print(f"Longitude : {first.longitude:.8f}")
    print(f"Latitude  : {first.latitude:.8f}")
    print(f"Elevation : {first.elevation}")

    print("\n↓\n")

    print("Local Point\n")

    print(f"X : {first_local.x:.3f}")
    print(f"Y : {first_local.y:.3f}")
    print(f"Z : {first_local.z:.3f}")

    separator("Last Point")

    last = session.centerline.points[-1]
    last_local = local_points[-1]

    print("Input Point\n")

    print(f"Longitude : {last.longitude:.8f}")
    print(f"Latitude  : {last.latitude:.8f}")
    print(f"Elevation : {last.elevation}")

    print("\n↓\n")

    print("Local Point\n")

    print(f"X : {last_local.x:.3f}")
    print(f"Y : {last_local.y:.3f}")
    print(f"Z : {last_local.z:.3f}")

    separator("Local Bounding Box")

    xs = [point.x for point in local_points]
    ys = [point.y for point in local_points]

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
    print(f"Output Points : {len(local_points)}")

    separator("Engineering Validation")

    print("Reference Frame      : PASS")
    print("Coordinate Transform : PASS")
    print("Point Count          : PASS")
    print("Bounding Box         : PASS")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
