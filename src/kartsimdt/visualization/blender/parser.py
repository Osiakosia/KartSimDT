from __future__ import annotations

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .curve import BlenderCurve
from .mapper import BlenderCurveMapper
from .validator import BlenderCurveValidator


class BlenderParser:

    def __init__(self) -> None:
        self._validator = BlenderCurveValidator()
        self._mapper = BlenderCurveMapper()

    def parse(
        self,
        session: TrackSurveySession,
    ) -> BlenderCurve:

        curve = self._mapper.map(session)

        self._validator.validate(curve)

        return curve
