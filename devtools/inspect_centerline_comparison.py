"""
inspect_centerline_comparison.py

KartSimDT Centerline Comparison Inspector
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.comparison.centerline_comparator import (
    CenterlineComparator,
)
from kartsimdt.survey.track_survey.mapper import TrackSurveyMapper
from kartsimdt.survey.track_survey.reader import KmlReader
from kartsimdt.survey.track_survey.validator import TrackSurveyValidator
from kartsimdt.visualization.geometry.centerline_mapper import (
    CenterlineGeometryMapper,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]


REFERENCE_DATASET = (
    PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
)

CANDIDATE_DATASET = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "aukstadvaris"
    / "survey"
    / "walked_centerline.kml"
)


def separator(
    title: str,
) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def load_geometry(
    dataset: Path,
):
    """
    Load centerline geometry.
    """

    reader = KmlReader()
    validator = TrackSurveyValidator()
    mapper = TrackSurveyMapper()
    geometry_mapper = CenterlineGeometryMapper()

    raw = reader.read(dataset)

    validator.validate(raw)

    session = mapper.map(raw)

    return geometry_mapper.map(session)


def main() -> None:
    """
    Inspect centerline comparison.
    """

    reference = load_geometry(
        REFERENCE_DATASET,
    )

    candidate = load_geometry(
        CANDIDATE_DATASET,
    )

    comparator = CenterlineComparator()

    result = comparator.compare(
        reference,
        candidate,
    )

    separator(
        "KartSimDT Centerline Comparison",
    )

    separator(
        "Reference",
    )

    print(f"File   : {REFERENCE_DATASET.name}")
    print(f"Points : {result.reference_points}")

    separator(
        "Candidate",
    )

    print(f"File   : {CANDIDATE_DATASET.name}")
    print(f"Points : {result.candidate_points}")

    separator(
        "Statistics",
    )

    print(f"Mean Error : {result.mean_error:.3f}")
    print(f"Max Error  : {result.max_error:.3f}")
    print(f"RMSE       : {result.rmse:.3f}")

    separator(
        "Comparison",
    )

    print("Pipeline : PASS")


if __name__ == "__main__":
    main()
