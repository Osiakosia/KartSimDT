"""
run_google_elevation.py

Retrieves Google terrain elevation for the
Aukstadvaris centerline and prints a table.
"""

from __future__ import annotations

import os
from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey_3d.google_elevation_client import (
    GoogleElevationClient,
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]


def main() -> None:
    track_file = (
        PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
    )

    api_key = os.environ.get("GOOGLE_ELEVATION_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GOOGLE_ELEVATION_API_KEY environment variable " "is not set."
        )

    survey = TrackSurveyParser().parse(
        track_file,
    )

    centerline_points = survey.centerline.points

    print()
    print("=" * 95)
    print("GOOGLE EARTH / GOOGLE ELEVATION PROFILE")
    print("=" * 95)

    print(
        f"{'Index':>6} "
        f"{'Latitude':>14} "
        f"{'Longitude':>14} "
        f"{'Elevation':>14} "
        f"{'Resolution':>14}"
    )

    print("-" * 95)

    client = GoogleElevationClient(
        api_key=api_key,
    )

    google_points = client.get_elevations(
        centerline_points,
    )

    for index, point in enumerate(
        google_points,
    ):
        resolution = f"{point.resolution:.3f}" if point.resolution is not None else "-"

        print(
            f"{index:6d} "
            f"{point.latitude:14.8f} "
            f"{point.longitude:14.8f} "
            f"{point.elevation:14.3f} "
            f"{resolution:>14}"
        )

    print("-" * 95)

    elevations = [point.elevation for point in google_points]

    print(f"{'POINTS':>6} " f"{len(google_points):>8}")

    print(f"{'MIN':>6} " f"{min(elevations):.3f} m")

    print(f"{'MAX':>6} " f"{max(elevations):.3f} m")

    print(f"{'RANGE':>6} " f"{max(elevations) - min(elevations):.3f} m")

    print("=" * 95)


if __name__ == "__main__":
    main()
