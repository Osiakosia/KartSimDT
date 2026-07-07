"""
validator.py

KartSimDT Track Survey Module

Validation of raw survey data.
"""

from __future__ import annotations

import math

from .exceptions import InvalidTrackSurveyError
from .raw import TrackSurveyRawData


class TrackSurveyValidator:
    """
    Validates TrackSurveyRawData before mapping.
    """

    def validate(
        self,
        raw: TrackSurveyRawData,
    ) -> None:
        """
        Validate raw survey data.
        """

        self._validate_metadata(raw)
        self._validate_coordinates(raw)

    def _validate_metadata(
        self,
        raw: TrackSurveyRawData,
    ) -> None:
        """
        Validate survey metadata.
        """

        if not raw.metadata:
            raise InvalidTrackSurveyError("Survey metadata is empty.")

        if not raw.metadata.get("name"):
            raise InvalidTrackSurveyError("Survey name is missing.")

    def _validate_coordinates(
        self,
        raw: TrackSurveyRawData,
    ) -> None:
        """
        Validate survey coordinates.
        """

        if not raw.coordinates:
            raise InvalidTrackSurveyError("Survey coordinates are empty.")

        if len(raw.coordinates) < 2:
            raise InvalidTrackSurveyError(
                "Survey must contain at least two coordinates."
            )

        for index, (longitude, latitude, elevation) in enumerate(
            raw.coordinates,
            start=1,
        ):
            self._validate_longitude(index, longitude)
            self._validate_latitude(index, latitude)
            self._validate_elevation(index, elevation)

    def _validate_longitude(
        self,
        index: int,
        longitude: float,
    ) -> None:
        """
        Validate longitude.
        """

        if math.isnan(longitude):
            raise InvalidTrackSurveyError(f"Longitude is NaN at point {index}.")

        if not -180.0 <= longitude <= 180.0:
            raise InvalidTrackSurveyError(
                f"Invalid longitude at point {index}: {longitude}"
            )

    def _validate_latitude(
        self,
        index: int,
        latitude: float,
    ) -> None:
        """
        Validate latitude.
        """

        if math.isnan(latitude):
            raise InvalidTrackSurveyError(f"Latitude is NaN at point {index}.")

        if not -90.0 <= latitude <= 90.0:
            raise InvalidTrackSurveyError(
                f"Invalid latitude at point {index}: {latitude}"
            )

    def _validate_elevation(
        self,
        index: int,
        elevation: float | None,
    ) -> None:
        """
        Validate elevation.
        """

        if elevation is None:
            return

        if math.isnan(elevation):
            raise InvalidTrackSurveyError(f"Elevation is NaN at point {index}.")
