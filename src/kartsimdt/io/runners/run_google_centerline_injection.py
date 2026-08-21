# """
# run_google_centerline_injection.py
#
# Inject Google Elevation API terrain elevation
# into the Track Survey centerline.
#
# Pipeline:
#
#     Centerline KML
#         ↓
#     TrackSurveyParser
#         ↓
#     GoogleElevationClient
#         ↓
#     ElevationProfile
#         ↓
#     Centerline elevation injection
#         ↓
#     3D Track Survey
# """
#
# from __future__ import annotations
#
# import os
# from pathlib import Path
#
# from kartsimdt.survey.track_survey.parser import TrackSurveyParser
#
# from kartsimdt.survey.track_survey_3d.elevation_profile import (
#     ElevationProfile,
#     ElevationProfilePoint,
# )
#
# from kartsimdt.survey.track_survey_3d.google_elevation_client import (
#     GoogleElevationClient,
# )
#
#
# PROJECT_ROOT = Path(__file__).resolve().parents[4]
#
#
# TRACK_FILE = (
#     PROJECT_ROOT
#     / "tests"
#     / "data"
#     / "aukstadvaris"
#     / "survey"
#     / "centerline.kml"
# )
#
#
# def build_google_profile(
#     survey,
#     api_key: str,
# ) -> ElevationProfile:
#     """
#     Retrieve Google terrain elevation for the
#     complete Track Survey centerline.
#     """
#
#     client = GoogleElevationClient(
#         api_key=api_key,
#     )
#
#     centerline_points = survey.centerline.points
#
#     google_points = client.get_elevations(
#         centerline_points,
#     )
#
#     expected_count = len(centerline_points)
#     actual_count = len(google_points)
#
#     if actual_count != expected_count:
#         raise RuntimeError(
#             "Google elevation result count mismatch: "
#             f"expected {expected_count}, "
#             f"got {actual_count}."
#         )
#
#     points = tuple(
#         ElevationProfilePoint(
#             survey_index=index,
#             elevation=google_point.elevation,
#             measurement_count=1,
#         )
#         for index, google_point in enumerate(
#             google_points
#         )
#     )
#
#     return ElevationProfile(
#         points=points,
#     )
#
#
# def inject_elevation_into_centerline(
#     survey,
#     profile: ElevationProfile,
# ) -> None:
#     """
#     Inject elevation profile values into the
#     existing Track Survey centerline.
#
#     Longitude and latitude are not modified.
#     """
#
#     centerline_points = survey.centerline.points
#
#     if len(centerline_points) != len(profile.points):
#         raise RuntimeError(
#             "Centerline/profile point count mismatch: "
#             f"centerline={len(centerline_points)}, "
#             f"profile={len(profile.points)}."
#         )
#
#     for profile_point in profile.points:
#         survey_index = profile_point.survey_index
#
#         if survey_index < 0:
#             raise RuntimeError(
#                 "Invalid negative survey index: "
#                 f"{survey_index}"
#             )
#
#         if survey_index >= len(centerline_points):
#             raise RuntimeError(
#                 "Elevation profile survey index is "
#                 "outside the centerline: "
#                 f"{survey_index}"
#             )
#
#         centerline_points[
#             survey_index
#         ].elevation = profile_point.elevation
#
#
# def validate_centerline_elevation(
#     survey,
# ) -> None:
#     """
#     Validate that every centerline point has elevation.
#     """
#
#     points = survey.centerline.points
#
#     if not points:
#         raise RuntimeError(
#             "Centerline contains no points."
#         )
#
#     missing_indices = [
#         index
#         for index, point in enumerate(points)
#         if point.elevation is None
#     ]
#
#     if missing_indices:
#         preview = missing_indices[:10]
#
#         raise RuntimeError(
#             "Centerline elevation injection incomplete. "
#             f"Missing {len(missing_indices)} points. "
#             f"First indices: {preview}"
#         )
#
#
# def print_elevation_summary(
#     survey,
# ) -> None:
#     """
#     Print basic elevation statistics for the
#     injected centerline.
#     """
#
#     elevations = [
#         point.elevation
#         for point in survey.centerline.points
#         if point.elevation is not None
#     ]
#
#     if not elevations:
#         raise RuntimeError(
#             "No elevation values available "
#             "after injection."
#         )
#
#     minimum = min(elevations)
#     maximum = max(elevations)
#
#     mean = sum(elevations) / len(elevations)
#
#     print()
#     print("-" * 72)
#     print("CENTERLINE ELEVATION SUMMARY")
#     print("-" * 72)
#
#     print(
#         f"Points       : {len(elevations)}",
#         flush=True,
#     )
#
#     print(
#         f"Minimum      : {minimum:.3f} m",
#         flush=True,
#     )
#
#     print(
#         f"Maximum      : {maximum:.3f} m",
#         flush=True,
#     )
#
#     print(
#         f"Elevation Δ  : {maximum - minimum:.3f} m",
#         flush=True,
#     )
#
#     print(
#         f"Mean         : {mean:.3f} m",
#         flush=True,
#     )
#
#
# def main() -> None:
#     print()
#     print("=" * 72)
#     print("KARTSIMDT — GOOGLE ELEVATION → CENTERLINE")
#     print("=" * 72)
#
#     # ---------------------------------------------------------
#     # Google API key
#     # ---------------------------------------------------------
#
#     api_key = os.environ.get(
#         "GOOGLE_ELEVATION_API_KEY",
#     )
#
#     if not api_key:
#         raise RuntimeError(
#             "GOOGLE_ELEVATION_API_KEY environment "
#             "variable is not set."
#         )
#
#     print()
#     print("Google Elevation API : OK")
#
#     # ---------------------------------------------------------
#     # Load Track Survey
#     # ---------------------------------------------------------
#
#     print()
#     print("-" * 72)
#     print("LOADING TRACK SURVEY")
#     print("-" * 72)
#
#     print(
#         f"Track file : {TRACK_FILE}",
#         flush=True,
#     )
#
#     if not TRACK_FILE.exists():
#         raise FileNotFoundError(
#             f"Track survey file not found: {TRACK_FILE}"
#         )
#
#     survey = TrackSurveyParser().parse(
#         TRACK_FILE,
#     )
#
#     centerline_count = len(
#         survey.centerline.points
#     )
#
#     if centerline_count == 0:
#         raise RuntimeError(
#             "Track Survey centerline contains no points."
#         )
#
#     print(
#         f"Centerline points : {centerline_count}",
#         flush=True,
#     )
#
#     # ---------------------------------------------------------
#     # Google Elevation
#     # ---------------------------------------------------------
#
#     print()
#     print("-" * 72)
#     print("BUILDING GOOGLE ELEVATION PROFILE")
#     print("-" * 72)
#
#     print(
#         "Requesting terrain elevation...",
#         flush=True,
#     )
#
#     google_profile = build_google_profile(
#         survey,
#         api_key,
#     )
#
#     google_count = google_profile.count()
#
#     print(
#         f"Google points     : {google_count}",
#         flush=True,
#     )
#
#     if google_count != centerline_count:
#         raise RuntimeError(
#             "Google profile does not match centerline "
#             "point count."
#         )
#
#     print(
#         "Google elevation  : OK",
#         flush=True,
#     )
#
#     # ---------------------------------------------------------
#     # Inject elevation
#     # ---------------------------------------------------------
#
#     print()
#     print("-" * 72)
#     print("INJECTING ELEVATION INTO CENTERLINE")
#     print("-" * 72)
#
#     print(
#         "Injecting Google terrain elevation...",
#         flush=True,
#     )
#
#     inject_elevation_into_centerline(
#         survey,
#         google_profile,
#     )
#
#     print(
#         "Elevation injection : OK",
#         flush=True,
#     )
#
#     # ---------------------------------------------------------
#     # Validate
#     # ---------------------------------------------------------
#
#     print()
#     print("-" * 72)
#     print("VALIDATING CENTERLINE")
#     print("-" * 72)
#
#     validate_centerline_elevation(
#         survey,
#     )
#
#     print(
#         "Centerline elevation : OK",
#         flush=True,
#     )
#
#     # ---------------------------------------------------------
#     # Summary
#     # ---------------------------------------------------------
#
#     print_elevation_summary(
#         survey,
#     )
#
#     # ---------------------------------------------------------
#     # Final result
#     # ---------------------------------------------------------
#
#     print()
#     print("=" * 72)
#     print("GOOGLE → CENTERLINE INJECTION COMPLETE")
#     print("=" * 72)
#
#     print(
#         f"Centerline points : {centerline_count}",
#         flush=True,
#     )
#
#     print(
#         "Elevation source   : Google Elevation API",
#         flush=True,
#     )
#
#     print(
#         "Centerline 3D      : READY",
#         flush=True,
#     )
#
#     print("=" * 72)
#
#
# if __name__ == "__main__":
#     main()

from __future__ import annotations

import os
from pathlib import Path

from kartsimdt.survey.track_survey.parser import TrackSurveyParser
from kartsimdt.survey.track_survey_3d.google_elevation_client import (
    GoogleElevationClient,
)
from kartsimdt.survey.track_survey_3d.google_elevation_kml_writer import (
    GoogleElevationKmlWriter,
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]

TRACK_FILE = (
    PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "aukstadvaris"
    / "survey"
    / "centerline_google_elevation.kml"
)


def main() -> None:
    print()
    print("=" * 72)
    print("KARTSIMDT — GOOGLE ELEVATION → FINAL TRACK SURVEY KML")
    print("=" * 72)

    api_key = os.environ.get(
        "GOOGLE_ELEVATION_API_KEY",
    )

    if not api_key:
        raise RuntimeError(
            "GOOGLE_ELEVATION_API_KEY environment " "variable is not set."
        )

    print()
    print("Google Elevation API : OK")

    # ---------------------------------------------------------
    # Load source Track Survey
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("LOADING TRACK SURVEY")
    print("-" * 72)

    print(
        f"Source KML : {TRACK_FILE}",
        flush=True,
    )

    if not TRACK_FILE.exists():
        raise FileNotFoundError(f"Track survey file not found: {TRACK_FILE}")

    survey = TrackSurveyParser().parse(
        TRACK_FILE,
    )

    centerline_points = survey.centerline.points

    if not centerline_points:
        raise RuntimeError("Track Survey centerline contains no points.")

    centerline_count = len(centerline_points)

    print(
        f"Centerline points : {centerline_count}",
        flush=True,
    )

    # ---------------------------------------------------------
    # Google Elevation
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("REQUESTING GOOGLE ELEVATION")
    print("-" * 72)

    client = GoogleElevationClient(
        api_key=api_key,
    )

    print(
        "Requesting terrain elevation...",
        flush=True,
    )

    google_points = client.get_elevations(
        centerline_points,
    )

    google_count = len(google_points)

    print(
        f"Google points     : {google_count}",
        flush=True,
    )

    if google_count != centerline_count:
        raise RuntimeError(
            "Google elevation result count mismatch: "
            f"centerline={centerline_count}, "
            f"google={google_count}"
        )

    print(
        "Google elevation  : OK",
        flush=True,
    )

    # ---------------------------------------------------------
    # Write final KML
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("BUILDING FINAL TRACK SURVEY KML")
    print("-" * 72)

    writer = GoogleElevationKmlWriter()

    writer.write(
        source_file=TRACK_FILE,
        elevations=google_points,
        output_file=OUTPUT_FILE,
    )

    print(
        f"Output KML : {OUTPUT_FILE}",
        flush=True,
    )

    print(
        "KML elevation injection : OK",
        flush=True,
    )

    # ---------------------------------------------------------
    # Validate final KML through normal Track Survey pipeline
    # ---------------------------------------------------------

    print()
    print("-" * 72)
    print("VALIDATING FINAL TRACK SURVEY")
    print("-" * 72)

    final_survey = TrackSurveyParser().parse(
        OUTPUT_FILE,
    )

    final_points = final_survey.centerline.points

    missing = [
        index for index, point in enumerate(final_points) if point.elevation is None
    ]

    if missing:
        raise RuntimeError(
            "Final Track Survey contains points without "
            f"elevation. Missing={len(missing)}, "
            f"first={missing[:10]}"
        )

    print(
        f"Final centerline points : {len(final_points)}",
        flush=True,
    )

    print(
        "Final elevation         : OK",
        flush=True,
    )

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    elevations = [
        point.elevation for point in final_points if point.elevation is not None
    ]

    minimum = min(elevations)
    maximum = max(elevations)
    mean = sum(elevations) / len(elevations)

    print()
    print("-" * 72)
    print("FINAL CENTERLINE ELEVATION SUMMARY")
    print("-" * 72)

    print(
        f"Points       : {len(elevations)}",
        flush=True,
    )

    print(
        f"Minimum      : {minimum:.3f} m",
        flush=True,
    )

    print(
        f"Maximum      : {maximum:.3f} m",
        flush=True,
    )

    print(
        f"Elevation Δ  : {maximum - minimum:.3f} m",
        flush=True,
    )

    print(
        f"Mean         : {mean:.3f} m",
        flush=True,
    )

    print()
    print("=" * 72)
    print("FINAL TRACK SURVEY KML READY")
    print("=" * 72)

    print(
        f"Output       : {OUTPUT_FILE}",
        flush=True,
    )

    print(
        "Track Survey : READY",
        flush=True,
    )

    print("=" * 72)


if __name__ == "__main__":
    main()
