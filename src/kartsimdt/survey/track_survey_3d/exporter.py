"""
exporter.py

Exports Track Survey 3D data to JSON.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from kartsimdt.survey.track_survey.session import TrackSurveySession

from .gps_dataset import GpsElevationDataset
from .matched_dataset import MatchedElevationDataset


class TrackSurvey3DExporter:
    """
    Exports Track Survey 3D data.
    """

    def export(
        self,
        survey: TrackSurveySession,
        matches: MatchedElevationDataset,
        gps_dataset: GpsElevationDataset,
        output_file: Path,
    ) -> None:
        data = self._build_json(
            survey,
            matches,
            gps_dataset,
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
                ensure_ascii=False,
            )

    def _to_float(
            self,
            value: float | str | None,
    ) -> float | None:
        if value is None:
            return None

        if isinstance(value, str):
            return float(value.replace(",", "."))

        return float(value)

    def _build_json(
        self,
        survey: TrackSurveySession,
        matches: MatchedElevationDataset,
        gps_dataset: GpsElevationDataset,
    ) -> dict:
        points = []

        for match in matches.matches:
            point = survey.centerline.points[match.survey_index]

            points.append(
                {
                    "survey_index": match.survey_index,
                    "longitude": point.longitude,
                    "latitude": point.latitude,
                    "elevation": self._to_float(point.elevation),
                    "match": {
                        "gps_longitude": match.gps_sample.longitude,
                        "gps_latitude": match.gps_sample.latitude,
                        "gps_elevation": self._to_float(match.gps_sample.elevation),
                        "session_index": match.gps_sample.session_index,
                        "distance_metres": match.distance_metres,
                    },
                }
            )

        session_count = max(sample.session_index for sample in gps_dataset.samples) + 1

        return {
            "format": "KartSimDT Track Survey 3D",
            "version": "1.0",
            "generated_at": datetime.now(
                UTC,
            ).isoformat(),
            "track": survey.metadata.name,
            "centerline_point_count": survey.centerline.count(),
            "gps_sample_count": gps_dataset.count(),
            "session_count": session_count,
            "points": points,
        }
