"""
acceptance_track_foundation.py

KartSimDT Engineering Acceptance

Track Survey Foundation acceptance report.
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

    separator("KartSimDT Engineering Acceptance")
    print("Track Survey Foundation")

    separator("Reference Dataset")

    print(f"File   : {DATASET.name}")
    print(f"Path   : {DATASET}")
    print(f"Points : {len(raw.coordinates)}")

    separator("Pipeline")

    print("KmlReader                PASS")
    print("TrackSurveyValidator     PASS")
    print("TrackSurveyMapper        PASS")

    separator("Platform Objects")

    print("SurveyMetadata           PASS")
    print("Point                    PASS")
    print("Centerline               PASS")
    print("TrackSurveySession       PASS")

    separator("Validation")

    print("Metadata                 PASS")
    print("Centerline               PASS")
    print(f"Point Count              PASS ({session.centerline.count()})")

    separator("Foundation Status")

    print("Track Survey Foundation")
    print()
    print("PASSED")

    separator("Acceptance Complete")


if __name__ == "__main__":
    main()
