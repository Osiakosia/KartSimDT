from __future__ import annotations

import math
from dataclasses import dataclass

from kartsimdt.survey.track_survey.session import TrackSurveySession


@dataclass(slots=True)
class LocalReferenceFrame:
    """
    Defines the local engineering coordinate system.
    """

    origin_longitude: float
    origin_latitude: float
    origin_elevation: float

    metres_per_degree_latitude: float
    metres_per_degree_longitude: float


def create_reference_frame(
    session: TrackSurveySession,
) -> LocalReferenceFrame:
    """
    Create a local engineering reference frame from
    a TrackSurveySession.
    """

    origin = session.centerline.points[0]

    return LocalReferenceFrame(
        origin_longitude=origin.longitude,
        origin_latitude=origin.latitude,
        origin_elevation=origin.elevation or 0.0,
        metres_per_degree_latitude=111320.0,
        metres_per_degree_longitude=(
            111320.0 * math.cos(math.radians(origin.latitude))
        ),
    )
