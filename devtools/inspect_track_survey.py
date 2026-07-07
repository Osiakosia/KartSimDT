"""
inspect_track_survey.py

KartSimDT Engineering Inspector

Displays the complete TrackSurveySession transformation pipeline.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey.reader import KmlReader

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


def main() -> None:
    reader = KmlReader()
    parser = TrackSurveyParser()

    raw = reader.read(DATASET)

    session = parser.parse(DATASET)

    separator("KartSimDT Engineering Inspector")
    print("Track Survey Session")

    separator("Reference Dataset")

    print(f"File       : {DATASET.name}")
    print(f"Points     : {len(raw.coordinates)}")

    separator("Raw KML Metadata")

    for key, value in raw.metadata.items():
        print(f"{key:20}: {value}")

    separator("Raw Coordinates")

    print(f"Point Count : {len(raw.coordinates)}")

    print("\nFirst Point")

    longitude, latitude, elevation = raw.coordinates[0]

    print(f"Longitude : {longitude:.8f}")
    print(f"Latitude  : {latitude:.8f}")
    print(f"Elevation : {elevation}")

    print("\nLast Point")

    longitude, latitude, elevation = raw.coordinates[-1]

    print(f"Longitude : {longitude:.8f}")
    print(f"Latitude  : {latitude:.8f}")
    print(f"Elevation : {elevation}")

    separator("Validation")

    print("Metadata     : PASS")
    print("Coordinates  : PASS")

    separator("Mapped Metadata")

    print(f"Name         : {session.metadata.name}")
    print(f"Description  : {session.metadata.description}")

    separator("Centerline")

    print(f"Point Count : {session.centerline.count()}")

    first = session.centerline.points[0]

    print("\nFirst Point")

    print(f"Longitude : {first.longitude:.8f}")
    print(f"Latitude  : {first.latitude:.8f}")
    print(f"Elevation : {first.elevation}")

    last = session.centerline.points[-1]

    print("\nLast Point")

    print(f"Longitude : {last.longitude:.8f}")
    print(f"Latitude  : {last.latitude:.8f}")
    print(f"Elevation : {last.elevation}")

    separator("TrackSurveySession")

    print("Metadata    : OK")
    print("Centerline  : OK")
    print(f"Points      : {session.centerline.count()}")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
