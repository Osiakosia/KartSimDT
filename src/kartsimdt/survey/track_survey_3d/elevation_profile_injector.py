"""
elevation_profile_injector.py

Injects an elevation profile into an existing Track Survey centerline.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .elevation_profile import ElevationProfile


class ElevationProfileInjector:
    """Inject an elevation profile into a Track Survey centerline."""

    def inject(
        self,
        survey: TrackSurveySession,
        profile: ElevationProfile,
    ) -> None:
        """
        Inject elevation values into centerline points.

        The profile's survey_index determines which centerline
        point receives each elevation value.
        """

        if not profile.points:
            raise ValueError("Elevation profile is empty.")

        centerline_count = survey.centerline.count()

        for profile_point in profile.points:
            index = profile_point.survey_index

            if index < 0 or index >= centerline_count:
                raise IndexError(
                    "Elevation profile survey index "
                    f"{index} is outside centerline range "
                    f"0..{centerline_count - 1}."
                )

            survey.centerline.points[index].elevation = profile_point.elevation
