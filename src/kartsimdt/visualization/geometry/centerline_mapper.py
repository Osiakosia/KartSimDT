"""
centerline_mapper.py

Maps Track Survey data into local centerline geometry.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)
from kartsimdt.visualization.geometry.coordinate_transform import (
    CoordinateTransform,
)
from kartsimdt.visualization.geometry.reference_frame import (
    create_reference_frame,
)


class CenterlineGeometryMapper:
    """
    Maps a TrackSurveySession into CenterlineGeometry.
    """

    def __init__(self) -> None:
        self._transform = CoordinateTransform()

    def map(
        self,
        session: TrackSurveySession,
    ) -> CenterlineGeometry:
        """
        Maps surveyed centerline points into the local
        engineering coordinate system.
        """

        frame = create_reference_frame(session)

        local_points = [
            self._transform.transform(
                point,
                frame,
            )
            for point in session.centerline.points
        ]

        return CenterlineGeometry(
            name=session.metadata.name,
            points=local_points,
        )
