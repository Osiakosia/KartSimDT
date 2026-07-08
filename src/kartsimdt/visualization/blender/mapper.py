"""
mapper.py

Maps a TrackSurveySession into a BlenderCurve.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .curve import BlenderCurve


class BlenderCurveMapper:
    """
    Maps a TrackSurveySession into a BlenderCurve.
    """

    def map(
        self,
        session: TrackSurveySession,
    ) -> BlenderCurve:
        """
        Create a BlenderCurve from a TrackSurveySession.
        """

        curve = BlenderCurve(
            name=session.metadata.name,
        )

        for point in session.centerline.points:

            curve.points.append(
                (
                    point.longitude,
                    point.latitude,
                    point.elevation or 0.0,
                ),
            )

        return curve
