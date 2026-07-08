"""
inspect_blender_curve.py

KartSimDT Engineering Inspector

Displays the BlenderCurve transformation pipeline.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.visualization.blender.mapper import BlenderCurveMapper

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

    parser = TrackSurveyParser()
    mapper = BlenderCurveMapper()

    session = parser.parse(DATASET)

    curve = mapper.map(session)

    separator("KartSimDT Blender Curve Inspector")

    separator("Reference Dataset")

    print(f"File       : {DATASET.name}")

    separator("TrackSurveySession")

    print(f"Survey Name : {session.metadata.name}")
    print(f"Point Count : {session.centerline.count()}")

    separator("Blender Curve")

    print(f"Curve Name  : {curve.name}")
    print(f"Point Count : {curve.count()}")

    first = curve.points[0]

    print("\nFirst Point")

    print(f"X : {first[0]:.8f}")
    print(f"Y : {first[1]:.8f}")
    print(f"Z : {first[2]:.3f}")

    last = curve.points[-1]

    print("\nLast Point")

    print(f"X : {last[0]:.8f}")
    print(f"Y : {last[1]:.8f}")
    print(f"Z : {last[2]:.3f}")

    separator("Statistics")

    print(f"Curve Points : {curve.count()}")

    separator("Pipeline")

    print("TrackSurveyParser   : OK")
    print("BlenderCurveMapper  : OK")
    print("BlenderCurve        : OK")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
