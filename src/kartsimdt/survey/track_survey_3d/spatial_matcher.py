"""
spatial_matcher.py

Matches Track Survey points with GPS elevation samples.
"""

from __future__ import annotations

import math

from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession

from .gps_dataset import GpsElevationDataset
from .gps_sample import GpsElevationSample
from .matched_dataset import MatchedElevationDataset
from .matched_elevation import MatchedElevation


class SpatialMatcher:
    """
    Matches Track Survey points with GPS elevation samples.
    """

    def match(
        self,
        survey: TrackSurveySession,
        dataset: GpsElevationDataset,
    ) -> MatchedElevationDataset:
        """
        Match all Track Survey points.
        """

        result = MatchedElevationDataset()

        for survey_index, survey_point in enumerate(
            survey.centerline.points,
        ):
            result.add(
                self._match_point(
                    survey_index,
                    survey_point,
                    dataset,
                )
            )

        return result

    def _match_point(
        self,
        survey_index: int,
        survey_point: Point,
        dataset: GpsElevationDataset,
    ) -> MatchedElevation:
        """
        Match one Track Survey point.
        """

        gps_sample, distance = self._find_nearest_sample(
            survey_point,
            dataset,
        )

        return MatchedElevation(
            survey_index=survey_index,
            survey_latitude=survey_point.latitude,
            survey_longitude=survey_point.longitude,
            gps_sample=gps_sample,
            distance_metres=distance,
        )

    def _find_nearest_sample(
        self,
        survey_point: Point,
        dataset: GpsElevationDataset,
    ) -> tuple[GpsElevationSample, float]:
        """
        Find the nearest GPS sample.
        """

        nearest = dataset.samples[0]

        nearest_distance = self._distance(
            survey_point,
            nearest,
        )

        for sample in dataset.samples[1:]:

            distance = self._distance(
                survey_point,
                sample,
            )

            if distance < nearest_distance:

                nearest = sample
                nearest_distance = distance

        return nearest, nearest_distance

    def _distance(
        self,
        survey_point: Point,
        gps_sample: GpsElevationSample,
    ) -> float:
        """
        Calculate the distance between two WGS84 points.

        Temporary implementation.
        Will be replaced by the Haversine formula.
        """

        dx = survey_point.longitude - gps_sample.longitude
        dy = survey_point.latitude - gps_sample.latitude

        return math.sqrt(dx * dx + dy * dy)
