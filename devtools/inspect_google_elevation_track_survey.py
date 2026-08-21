from __future__ import annotations

from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TRACK_FILE = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "aukstadvaris"
    / "survey"
    / "centerline_google_elevation.kml"
)


def main() -> None:
    print("=" * 72)
    print("KARTSIMDT — TRACK SURVEY GOOGLE ELEVATION CHECK")
    print("=" * 72)

    print()
    print(f"Input KML : {TRACK_FILE}")

    if not TRACK_FILE.exists():
        raise FileNotFoundError(f"Track Survey KML not found: {TRACK_FILE}")

    survey = TrackSurveyParser().parse(TRACK_FILE)

    points = survey.centerline.points

    if not points:
        raise RuntimeError("Track Survey centerline contains no points.")

    missing = [index for index, point in enumerate(points) if point.elevation is None]

    elevations = [
        float(point.elevation) for point in points if point.elevation is not None
    ]

    print()
    print("TRACK SURVEY")
    print("-" * 72)
    print(f"Track name       : {survey.metadata.name}")
    print(f"Centerline points: {len(points)}")
    print(f"Elevation points : {len(elevations)}")
    print(f"Missing elevation: {len(missing)}")

    if missing:
        print(f"First missing    : {missing[:10]}")
        raise RuntimeError(
            "Track Survey does not contain elevation " "for every centerline point."
        )

    print()
    print("ELEVATION")
    print("-" * 72)
    print(f"Minimum          : {min(elevations):.3f} m")
    print(f"Maximum          : {max(elevations):.3f} m")
    print(f"Elevation Δ      : " f"{max(elevations) - min(elevations):.3f} m")
    print(f"Mean             : {sum(elevations) / len(elevations):.3f} m")

    print()
    print("SAMPLE POINTS")
    print("-" * 72)

    for index in (
        0,
        len(points) // 2,
        len(points) - 1,
    ):
        point = points[index]

        print(
            f"[{index:03d}] "
            f"lon={point.longitude:.7f} "
            f"lat={point.latitude:.7f} "
            f"elevation={point.elevation:.3f} m"
        )

    print()
    print("=" * 72)
    print("TRACK SURVEY GOOGLE ELEVATION : OK")
    print("=" * 72)


if __name__ == "__main__":
    main()
