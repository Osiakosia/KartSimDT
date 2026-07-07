"""
mapper.py

KartSimDT Track Survey Module

Maps validated survey data into the Track Survey domain model.
"""

from __future__ import annotations

from .centerline import Centerline
from .metadata import SurveyMetadata
from .point import Point
from .raw import TrackSurveyRawData
from .session import TrackSurveySession


class TrackSurveyMapper:
    """
    Maps TrackSurveyRawData into TrackSurveySession.
    """

    def map(
        self,
        raw: TrackSurveyRawData,
    ) -> TrackSurveySession:
        """
        Map validated raw survey data.
        """

        metadata = self._map_metadata(raw)

        centerline = self._map_centerline(raw)

        return TrackSurveySession(
            metadata=metadata,
            centerline=centerline,
        )

    def _map_metadata(
        self,
        raw: TrackSurveyRawData,
    ) -> SurveyMetadata:
        """
        Map survey metadata.
        """

        return SurveyMetadata(
            name=raw.metadata.get("name", ""),
            description=raw.metadata.get("description", ""),
        )

    def _map_centerline(
        self,
        raw: TrackSurveyRawData,
    ) -> Centerline:
        """
        Map survey coordinates into a centerline.
        """

        points = [
            Point(
                longitude=longitude,
                latitude=latitude,
                elevation=elevation,
            )
            for longitude, latitude, elevation in raw.coordinates
        ]

        return Centerline(
            points=points,
        )
