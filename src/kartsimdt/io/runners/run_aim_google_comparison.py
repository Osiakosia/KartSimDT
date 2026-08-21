"""
Compare AIM median elevation with Google Elevation API
for the Aukstadvaris karting track.
"""

from __future__ import annotations

import os
from pathlib import Path

from kartsimdt.io.aim.parser import AimTelemetryParser
from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.elevation_profile import (
    ElevationProfile,
    ElevationProfilePoint,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_builder import (
    ElevationProfileBuilder,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_comparator import (
    ElevationProfileComparator,
    ElevationProfileComparison,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_normalizer import (
    ElevationProfileNormalizer,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_plotter import (
    ElevationProfilePlotter,
)
from kartsimdt.survey.track_survey_3d.full_lap_extractor import (
    FullLapExtractor,
)
from kartsimdt.survey.track_survey_3d.google_elevation_client import (
    GoogleElevationClient,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile import (
    LapElevationProfile,
)
from kartsimdt.survey.track_survey_3d.lap_elevation_profile_normalizer import (
    LapElevationProfileNormalizer,
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


def build_aim_profile(
    survey: TrackSurveySession,
) -> ElevationProfile:
    """Build the AIM median elevation profile."""

    telemetry_dir = PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "aim"

    telemetry_files = [
        telemetry_dir / "session_01.csv",
        telemetry_dir / "session_02.csv",
        telemetry_dir / "session_03.csv",
        telemetry_dir / "session_04.csv",
        telemetry_dir / "session_05.csv",
    ]

    parser = AimTelemetryParser()
    extractor = FullLapExtractor()
    policy = LapSelectionPolicy()
    gps_builder = LapGpsDatasetBuilder()
    matcher = SpatialMatcher()
    lap_normalizer = LapElevationProfileNormalizer()
    profile_builder = ElevationProfileBuilder()

    normalized_profiles = []

    for session_index, telemetry_file in enumerate(
        telemetry_files,
        start=1,
    ):
        print(f"AIM session {session_index}/" f"{len(telemetry_files)}")

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

        print(f"selected laps: " f"{len(selected_laps)}")

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

            normalized_profile = lap_normalizer.normalize(
                profile,
            )

            normalized_profiles.append(normalized_profile)

    print(f"normalized AIM profiles: " f"{len(normalized_profiles)}")

    return profile_builder.build(
        normalized_profiles,
    )


def build_google_profile(
    survey: TrackSurveySession,
    api_key: str,
) -> ElevationProfile:
    """Build the Google elevation profile."""

    client = GoogleElevationClient(
        api_key=api_key,
    )

    google_points = client.get_elevations(
        survey.centerline.points,
    )

    expected_count = len(survey.centerline.points)

    actual_count = len(google_points)

    if actual_count != expected_count:
        raise RuntimeError(
            "Google elevation result count mismatch: "
            f"expected {expected_count}, "
            f"got {actual_count}."
        )

    points = tuple(
        ElevationProfilePoint(
            survey_index=index,
            elevation=google_point.elevation,
            measurement_count=1,
        )
        for index, google_point in enumerate(
            google_points,
        )
    )

    return ElevationProfile(
        points=points,
    )


def print_comparison_results(
    comparison: ElevationProfileComparison,
) -> None:
    """Print final AIM vs Google comparison results."""

    print()
    print("=" * 72)
    print("AIM VS GOOGLE COMPARISON RESULTS")
    print("=" * 72)

    print(
        "Points                 : " f"{comparison.point_count}",
        flush=True,
    )

    print(
        "MAE                    : " f"{comparison.mae:.3f} m",
        flush=True,
    )

    print(
        "RMSE                   : " f"{comparison.rmse:.3f} m",
        flush=True,
    )

    print(
        "Maximum absolute error : " f"{comparison.max_absolute_error:.3f} m",
        flush=True,
    )

    print(
        "Correlation            : " f"{comparison.correlation:.6f}",
        flush=True,
    )

    print(
        "=" * 72,
        flush=True,
    )


def main() -> None:
    print()
    print("=" * 72)
    print("AUKŠTADVARIS — AIM VS GOOGLE ELEVATION")
    print("=" * 72)

    # ---------------------------------------------------------
    # Google API key
    # ---------------------------------------------------------

    api_key = os.environ.get(
        "GOOGLE_ELEVATION_API_KEY",
    )

    if not api_key:
        raise RuntimeError(
            "GOOGLE_ELEVATION_API_KEY environment " "variable is not set."
        )

    # ---------------------------------------------------------
    # Centerline
    # ---------------------------------------------------------

    track_file = (
        PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
    )

    survey = TrackSurveyParser().parse(
        track_file,
    )

    centerline_count = len(survey.centerline.points)

    print(f"Centerline points : " f"{centerline_count}")

    # ---------------------------------------------------------
    # AIM
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("BUILDING AIM MEDIAN PROFILE")
    print("-" * 72)

    aim_profile = build_aim_profile(
        survey,
    )

    print()
    print(f"AIM points        : " f"{len(aim_profile.points)}")

    # ---------------------------------------------------------
    # Google
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("BUILDING GOOGLE ELEVATION PROFILE")
    print("-" * 72)

    google_profile = build_google_profile(
        survey,
        api_key,
    )

    print(f"Google points     : " f"{len(google_profile.points)}")

    # ---------------------------------------------------------
    # Normalization
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("NORMALIZATION")
    print("-" * 72)

    normalizer = ElevationProfileNormalizer()

    normalized_aim = normalizer.normalize(
        aim_profile,
    )

    print("AIM normalized    : OK")

    normalized_google = normalizer.normalize(
        google_profile,
    )

    print("Google normalized : OK")

    # ---------------------------------------------------------
    # Validate normalized profiles
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("VALIDATING PROFILES")
    print("-" * 72)

    print(f"AIM normalized points    : " f"{len(normalized_aim.points)}")

    print(f"Google normalized points : " f"{len(normalized_google.points)}")

    if len(normalized_aim.points) != centerline_count:
        raise RuntimeError(
            "AIM normalized profile must contain " f"{centerline_count} points."
        )

    if len(normalized_google.points) != centerline_count:
        raise RuntimeError(
            "Google normalized profile must contain " f"{centerline_count} points."
        )

    print("Point count validation   : OK")

    plotter = ElevationProfilePlotter()

    plot_output = (
        PROJECT_ROOT
        / "tests"
        / "data"
        / "plots"
        / "aukstadvaris_aim_google_elevation.png"
    )

    plotter.plot_comparison(
        aim=normalized_aim,
        google=normalized_google,
        output_path=plot_output,
        show=False,
    )

    print(f"Elevation comparison plot saved: " f"{plot_output}")

    # ---------------------------------------------------------
    # Comparison
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("COMPARISON")
    print("-" * 72)

    print("Creating comparator...")

    comparator = ElevationProfileComparator()

    print("Calling comparator.compare()...")

    try:
        comparison = comparator.compare(
            reference=normalized_aim,
            candidate=normalized_google,
        )
    except Exception as exc:
        print()
        print("!!! COMPARATOR FAILED !!!")
        print(f"{type(exc).__name__}: {exc}")
        raise

    print(
        "Comparator finished : OK",
        flush=True,
    )

    print(
        "RESULT CALL START",
        flush=True,
    )

    print(
        "POINT COUNT =",
        comparison.point_count,
        flush=True,
    )

    print(
        "MAE =",
        comparison.mae,
        flush=True,
    )

    print(
        "RMSE =",
        comparison.rmse,
        flush=True,
    )

    print(
        "MAX =",
        comparison.max_absolute_error,
        flush=True,
    )

    print(
        "CORRELATION =",
        comparison.correlation,
        flush=True,
    )

    print(
        "RESULT CALL END",
        flush=True,
    )


if __name__ == "__main__":
    main()
