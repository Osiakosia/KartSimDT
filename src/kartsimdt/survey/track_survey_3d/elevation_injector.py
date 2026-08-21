"""
elevation_injector.py

Injects matched GPS elevation values into Track Survey points.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .matched_dataset import MatchedElevationDataset


class ElevationInjector:
    """
    Injects matched GPS elevations into an existing Track Survey.
    """

    def inject(
        self,
        survey: TrackSurveySession,
        matches: MatchedElevationDataset,
    ) -> None:
        """
        Inject matched elevation values into Track Survey points.

        Longitude and latitude coordinates are not modified.
        """

        for match in matches.matches:
            point = survey.centerline.points[match.survey_index]

            point.elevation = match.gps_sample.elevation
