"""
inspect_track_survey_validator.py

KartSimDT Engineering Inspector

Validates the reference Track Survey dataset.
"""

from __future__ import annotations

from pathlib import Path

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

    separator("KartSimDT Track Survey Validator")

    print(f"File : {DATASET.name}")
    print(f"Path : {DATASET}")

    reader = KmlReader()
    validator = TrackSurveyValidator()

    raw = reader.read(DATASET)

    separator("Raw Survey Data")

    print(f"Name        : {raw.metadata.get('name')}")
    print(f"Description : {raw.metadata.get('description')}")
    print(f"Coordinates : {len(raw.coordinates)}")

    separator("Validation")

    validator.validate(raw)

    print("Metadata      : PASS")
    print("Coordinates   : PASS")
    print("Coordinate Range : PASS")

    separator("Validation Complete")


if __name__ == "__main__":
    main()
