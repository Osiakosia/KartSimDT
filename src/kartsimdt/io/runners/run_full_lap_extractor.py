"""
run_full_lap_extractor.py

Runs FullLapExtractor on real AIM telemetry sessions
and builds elevation profiles.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from kartsimdt.io.aim.parser import AimTelemetryParser
from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey_3d.elevation_profile_builder import (
    ElevationProfileBuilder,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_calculator import (
    ElevationProfileCalculator,
)
from kartsimdt.survey.track_survey_3d.full_lap_extractor import (
    FullLapExtractor,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile_analyzer import (
    LapElevationProfileAnalyzer,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile_normalizer import (
    LapElevationProfileNormalizer,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profiles import (
    LapElevationProfileCollection,
)
from kartsimdt.survey.track_survey_3d.lap_gps_dataset_builder import (
    LapGpsDatasetBuilder,
)
from kartsimdt.survey.track_survey_3d.lap_selection_policy import (
    LapSelectionPolicy,
)
from kartsimdt.survey.track_survey_3d.spatial_matcher import (
    SpatialMatcher,
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]


def main() -> None:
    # ---------------------------------------------------------
    # Track survey
    # ---------------------------------------------------------

    track_file = (
        PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
    )

    survey = TrackSurveyParser().parse(
        track_file,
    )

    # ---------------------------------------------------------
    # Calculate centerline elevation profile
    # ---------------------------------------------------------

    elevation_calculator = ElevationProfileCalculator()

    centerline_elevation_profile = elevation_calculator.calculate(
        survey.centerline,
    )

    # ---------------------------------------------------------
    # AIM telemetry files
    # ---------------------------------------------------------

    telemetry_dir = PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "aim"

    telemetry_files = [
        telemetry_dir / "session_01.csv",
        telemetry_dir / "session_02.csv",
        telemetry_dir / "session_03.csv",
        telemetry_dir / "session_04.csv",
        telemetry_dir / "session_05.csv",
    ]

    print()
    print("AIM sessions:")

    for telemetry_file in telemetry_files:
        print(f"  {telemetry_file.name}")

    print(f"Total: {len(telemetry_files)}")

    # ---------------------------------------------------------
    # Components
    # ---------------------------------------------------------

    parser = AimTelemetryParser()
    extractor = FullLapExtractor()
    policy = LapSelectionPolicy()
    gps_builder = LapGpsDatasetBuilder()
    matcher = SpatialMatcher()
    analyzer = LapElevationProfileAnalyzer()
    normalizer = LapElevationProfileNormalizer()
    profile_builder = ElevationProfileBuilder()

    profiles = LapElevationProfileCollection()

    # ---------------------------------------------------------
    # Extract and match full laps
    # ---------------------------------------------------------

    print()
    print("=" * 60)
    print("LAP ELEVATION PROFILE COLLECTION")
    print("=" * 60)

    for session_index, telemetry_file in enumerate(
        telemetry_files,
    ):
        session = parser.parse(
            telemetry_file,
        )

        full_laps = extractor.extract(
            session=session,
            session_index=session_index,
        )

        selected_laps = policy.select(
            full_laps,
        )

        print()
        print(f"Session {session_index + 1}")
        print(f"File          : {telemetry_file.name}")
        print(f"Full laps     : {len(full_laps)}")
        print(f"Selected laps : {len(selected_laps)}")
        print("Lap numbers   : " f"{[lap.lap_number for lap in selected_laps]}")

        for lap in selected_laps:
            gps_dataset = gps_builder.build(
                session=session,
                lap=lap,
            )

            matches = matcher.match(
                survey=survey,
                dataset=gps_dataset,
            )

            profile = LapElevationProfile(
                session_index=session_index,
                lap_number=lap.lap_number,
                matches=matches,
            )

            profiles.add(
                profile,
            )

            print(
                f"  Lap {lap.lap_number:2d} : "
                f"{lap.duration:7.3f} s "
                f"GPS={gps_dataset.count():4d} "
                f"Matches={matches.count():3d}"
            )

    # ---------------------------------------------------------
    # Collection summary
    # ---------------------------------------------------------

    print()
    print("=" * 60)
    print("COLLECTION SUMMARY")
    print("=" * 60)

    print(f"Sessions           : " f"{len(telemetry_files)}")

    print(f"Profiles           : " f"{profiles.count()}")

    if profiles.count() == 0:
        print("=" * 60)
        return

    first_profile = next(
        iter(profiles),
    )

    print(f"Points per profile : " f"{first_profile.count()}")

    total_measurements = sum(profile.count() for profile in profiles)

    print(f"Measurements       : " f"{total_measurements}")

    # ---------------------------------------------------------
    # AIM elevation profile statistics
    # ---------------------------------------------------------

    print()
    print("=" * 72)
    print("ELEVATION PROFILE STATISTICS")
    print("=" * 72)

    print(
        f"{'Session':>7} "
        f"{'Lap':>4} "
        f"{'Points':>7} "
        f"{'Min':>10} "
        f"{'Max':>10} "
        f"{'Mean':>10}"
    )

    print("-" * 72)

    for profile in profiles:
        stats = analyzer.analyze(
            profile,
        )

        print(
            f"{stats.session_index + 1:7d} "
            f"{stats.lap_number:4d} "
            f"{stats.point_count:7d} "
            f"{stats.minimum_elevation:10.3f} "
            f"{stats.maximum_elevation:10.3f} "
            f"{stats.mean_elevation:10.3f}"
        )

    # ---------------------------------------------------------
    # Centerline elevation profile
    # ---------------------------------------------------------

    print()
    print("=" * 72)
    print("CENTERLINE ELEVATION PROFILE")
    print("=" * 72)

    print(
        f"{'Point':>7} "
        f"{'Distance':>12} "
        f"{'Elevation':>12} "
        f"{'Delta':>12} "
        f"{'Grade':>10}"
    )

    print("-" * 72)

    for index, point in enumerate(
        centerline_elevation_profile,
    ):
        print(
            f"{index:7d} "
            f"{point.distance_metres:12.3f} "
            f"{point.elevation:12.3f} "
            f"{point.delta_elevation:12.3f} "
            f"{point.grade_percent:10.3f}%"
        )

    print("=" * 72)

    # ---------------------------------------------------------
    # Build combined normalized elevation profile
    # ---------------------------------------------------------

    normalized_profiles = [normalizer.normalize(profile) for profile in profiles]

    combined_elevation_profile = profile_builder.build(
        normalized_profiles,
    )

    # ---------------------------------------------------------
    # Extract combined profile values
    # ---------------------------------------------------------

    elevations = [point.elevation for point in combined_elevation_profile.points]

    measurement_counts = [
        point.measurement_count for point in combined_elevation_profile.points
    ]

    x = [point.survey_index for point in combined_elevation_profile.points]

    y = [point.elevation for point in combined_elevation_profile.points]

    # ---------------------------------------------------------
    # Plot combined AIM elevation profile
    # ---------------------------------------------------------

    plt.figure(
        figsize=(14, 6),
    )

    plt.plot(
        x,
        y,
        linewidth=1.5,
    )

    plt.axhline(
        0.0,
        linewidth=0.8,
    )

    plt.title("Aukštadvaris - AIM Median Elevation Profile")

    plt.xlabel("Centerline point index")

    plt.ylabel("Relative elevation [m]")

    plt.grid(
        True,
        alpha=0.3,
    )

    plt.tight_layout()
    plt.show()

    # ---------------------------------------------------------
    # Combined profile summary
    # ---------------------------------------------------------

    print()
    print("=" * 60)
    print("COMBINED ELEVATION PROFILE")
    print("=" * 60)

    print(f"Profiles            : " f"{len(normalized_profiles)}")

    print(f"Centerline points   : " f"{combined_elevation_profile.count()}")

    print(
        f"Measurements/point : "
        f"{min(measurement_counts)}.."
        f"{max(measurement_counts)}"
    )

    print(f"Elevation min       : " f"{min(elevations):.3f} m")

    print(f"Elevation max       : " f"{max(elevations):.3f} m")

    print(f"Elevation range     : " f"{max(elevations) - min(elevations):.3f} m")

    print("=" * 60)


if __name__ == "__main__":
    main()
