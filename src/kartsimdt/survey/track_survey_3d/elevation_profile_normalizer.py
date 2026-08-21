"""
Normalization of source-neutral elevation profiles.
"""

from __future__ import annotations

from statistics import fmean

from kartsimdt.survey.track_survey_3d.elevation_profile import (
    ElevationProfile,
    ElevationProfilePoint,
)


class ElevationProfileNormalizer:
    """Normalize an elevation profile by removing its mean elevation."""

    def normalize(
        self,
        profile: ElevationProfile,
    ) -> ElevationProfile:
        if not profile.points:
            return ElevationProfile(
                points=(),
            )

        mean_elevation = fmean(point.elevation for point in profile.points)

        normalized_points = tuple(
            ElevationProfilePoint(
                survey_index=point.survey_index,
                elevation=point.elevation - mean_elevation,
                measurement_count=point.measurement_count,
            )
            for point in profile.points
        )

        return ElevationProfile(
            points=normalized_points,
        )
