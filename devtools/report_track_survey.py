"""
report_track_survey.py

KartSimDT Track Survey Report

Displays the TrackSurveySession domain object.

============================================================
TrackSurveySession Summary
============================================================

Metadata     ✓

Centerline   ✓

Points       677

"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import KmlReader
from kartsimdt.survey.track_survey.validator import TrackSurveyValidator

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
    mapper = TrackSurveyMapper()

    raw = reader.read(DATASET)
    validator.validate(raw)
    session = mapper.map(raw)

    separator("KartSimDT Track Survey Report")

    separator("TrackSurveySession")

    print("Object : TrackSurveySession")

    separator("SurveyMetadata")

    print(f"Name        : {session.metadata.name}")
    print(f"Description : {session.metadata.description}")

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

    longitudes = [point.longitude for point in session.centerline.points]
    latitudes = [point.latitude for point in session.centerline.points]

    separator("Bounding Box")

    print(f"North : {max(latitudes):.8f}")
    print(f"South : {min(latitudes):.8f}")
    print(f"East  : {max(longitudes):.8f}")
    print(f"West  : {min(longitudes):.8f}")

    separator("Platform Objects")

    print("SurveyMetadata      : OK")
    print("Centerline          : OK")
    print(f"Point               : {session.centerline.count()}")
    print("TrackSurveySession  : OK")

    separator("Reference Dataset")

    print(f"File : {DATASET.name}")

    separator("Future Extensions")

    print("Critical Points : pending")
    print("Photos          : pending")
    print("Notes           : pending")
    print("Elevation       : pending (Telemetry)")

    separator("Report Complete")


if __name__ == "__main__":
    main()
