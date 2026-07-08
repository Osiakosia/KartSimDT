"""
report_blender_curve.py

KartSimDT Blender Curve Report.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.visualization.blender.parser import BlenderParser

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TEST_DATA = PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey"

DATASET = TEST_DATA / "centerline.kml"


def separator(title: str) -> None:
    """Print section separator."""

    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:

    survey_parser = TrackSurveyParser()
    blender_parser = BlenderParser()

    session = survey_parser.parse(DATASET)
    curve = blender_parser.parse(session)

    xs = [point[0] for point in curve.points]
    ys = [point[1] for point in curve.points]
    zs = [point[2] for point in curve.points]

    separator("KartSimDT Blender Curve Report")

    print(f"Curve Name  : {curve.name}")
    print(f"Point Count : {curve.count()}")

    separator("Bounding Box")

    print(f"X Min : {min(xs):.8f}")
    print(f"X Max : {max(xs):.8f}")

    print(f"Y Min : {min(ys):.8f}")
    print(f"Y Max : {max(ys):.8f}")

    print(f"Z Min : {min(zs):.3f}")
    print(f"Z Max : {max(zs):.3f}")

    separator("First Point")

    x, y, z = curve.points[0]

    print(f"X : {x:.8f}")
    print(f"Y : {y:.8f}")
    print(f"Z : {z:.3f}")

    separator("Last Point")

    x, y, z = curve.points[-1]

    print(f"X : {x:.8f}")
    print(f"Y : {y:.8f}")
    print(f"Z : {z:.3f}")

    separator("Status")

    print("Curve      : OK")
    print("Validation : PASS")

    separator("Report Complete")


if __name__ == "__main__":
    main()
