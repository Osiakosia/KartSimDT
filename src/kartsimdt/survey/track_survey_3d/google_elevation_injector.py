"""
google_elevation_injector.py

Injects raw Google terrain elevation into
Track Survey centerline points.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .google_elevation_client import GoogleElevationPoint


class GoogleElevationInjector:
    """
    Inject Google terrain elevation into an existing
    Track Survey centerline.
    """

    def inject(
        self,
        survey: TrackSurveySession,
        elevations: list[GoogleElevationPoint],
    ) -> int:
        """
        Inject Google elevation into centerline points.

        The order of GoogleElevationPoint objects must match
        the order of Track Survey centerline points.

        Longitude and latitude are not modified.

        Returns
        -------
        int
            Number of centerline points updated.
        """

        centerline_points = survey.centerline.points

        if not centerline_points:
            raise ValueError("Cannot inject elevation into an empty centerline.")

        if not elevations:
            raise ValueError("Cannot inject an empty Google elevation dataset.")

        if len(centerline_points) != len(elevations):
            raise ValueError(
                "Centerline and Google elevation data must "
                "contain the same number of points. "
                f"Centerline={len(centerline_points)}, "
                f"Google={len(elevations)}."
            )

        for index, google_point in enumerate(elevations):
            centerline_point = centerline_points[index]

            centerline_point.elevation = google_point.elevation

        return len(elevations)
