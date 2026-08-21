"""
run_track_survey_3d.py

Real Track Survey 3D integration runner.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.parser import AimTelemetryParser
from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey_3d.elevation_injector import (
    ElevationInjector,
)
from kartsimdt.survey.track_survey_3d.exporter import (
    TrackSurvey3DExporter,
)
from kartsimdt.survey.track_survey_3d.gps_dataset_builder import (
    GpsDatasetBuilder,
)
from kartsimdt.survey.track_survey_3d.spatial_matcher import (
    SpatialMatcher,
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]


def main() -> None:
    track_file = (
        PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
    )

    telemetry_dir = PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "aim"

    telemetry_files = sorted(telemetry_dir.glob("session_*.csv"))

    survey = TrackSurveyParser().parse(
        track_file,
    )

    for telemetry_file in telemetry_files:
        print(
            telemetry_file,
            telemetry_file.exists(),
        )
    telemetry_parser = AimTelemetryParser()

    telemetry_sessions = [telemetry_parser.parse(path) for path in telemetry_files]

    dataset = GpsDatasetBuilder().build(
        telemetry_sessions,
    )

    matcher = SpatialMatcher()

    matches = matcher.match(
        survey,
        dataset,
    )

    injector = ElevationInjector()

    injector.inject(
        survey,
        matches,
    )
    output_file = (
        PROJECT_ROOT
        / "data"
        / "tracks"
        / "Aukštadvaris"
        / "final"
        / "track_survey_3d.json"
    )

    exporter = TrackSurvey3DExporter()

    exporter.export(
        survey=survey,
        matches=matches,
        gps_dataset=dataset,
        output_file=output_file,
    )

    elevations = [
        point.elevation
        for point in survey.centerline.points
        if point.elevation is not None
    ]

    print()
    print("=" * 60)
    print("TRACK SURVEY 3D")
    print("=" * 60)

    print(f"Track              : {survey.metadata.name}")
    print(f"Centerline points  : {survey.centerline.count()}")
    print(f"Telemetry sessions : {len(telemetry_sessions)}")
    print(f"GPS samples        : {dataset.count()}")
    print(f"Matched points     : {matches.count()}")
    print(f"Injected points    : {len(elevations)}")

    if elevations:
        print()

        numeric_elevations = [
            float(str(value).replace(",", ".")) for value in elevations
        ]

        print(f"Minimum elevation  : {min(numeric_elevations):.3f} m")
        print(f"Maximum elevation  : {max(numeric_elevations):.3f} m")

        print()
        print(f"Exported JSON      : {output_file}")

    print("=" * 60)


if __name__ == "__main__":
    main()
