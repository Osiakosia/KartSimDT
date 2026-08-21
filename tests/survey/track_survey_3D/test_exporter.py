"""
test_exporter.py

Tests for TrackSurvey3DExporter.
"""

from __future__ import annotations

import json
from pathlib import Path

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.metadata import SurveyMetadata
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.exporter import (
    TrackSurvey3DExporter,
)
from kartsimdt.survey.track_survey_3d.gps_dataset import (
    GpsElevationDataset,
)
from kartsimdt.survey.track_survey_3d.gps_sample import (
    GpsElevationSample,
)
from kartsimdt.survey.track_survey_3d.matched_dataset import (
    MatchedElevationDataset,
)
from kartsimdt.survey.track_survey_3d.matched_elevation import (
    MatchedElevation,
)


def test_export_track_survey_3d(
    tmp_path: Path,
) -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Aukstadvaris",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=24.001000,
                    latitude=54.001000,
                    elevation=176.42,
                ),
                Point(
                    longitude=24.002000,
                    latitude=54.002000,
                    elevation=177.31,
                ),
            ],
        ),
    )

    gps_sample_0 = GpsElevationSample(
        longitude=24.001001,
        latitude=54.001001,
        elevation=176.42,
        session_index=0,
    )

    gps_sample_1 = GpsElevationSample(
        longitude=24.002002,
        latitude=54.002001,
        elevation=177.31,
        session_index=1,
    )

    gps_dataset = GpsElevationDataset()

    gps_dataset.add(gps_sample_0)
    gps_dataset.add(gps_sample_1)

    matches = MatchedElevationDataset()

    matches.add(
        MatchedElevation(
            survey_index=0,
            survey_longitude=24.001000,
            survey_latitude=54.001000,
            gps_sample=gps_sample_0,
            distance_metres=0.13,
        )
    )

    matches.add(
        MatchedElevation(
            survey_index=1,
            survey_longitude=24.002000,
            survey_latitude=54.002000,
            gps_sample=gps_sample_1,
            distance_metres=0.17,
        )
    )

    output_file = tmp_path / "track_survey_3d.json"

    exporter = TrackSurvey3DExporter()

    exporter.export(
        survey=survey,
        matches=matches,
        gps_dataset=gps_dataset,
        output_file=output_file,
    )

    assert output_file.exists()

    with output_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    print("\n========== TRACK SURVEY 3D JSON ==========")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print("==========================================")

    assert data["format"] == "KartSimDT Track Survey 3D"
    assert data["version"] == "1.0"

    assert "generated_at" in data

    assert data["track"] == "Aukstadvaris"

    assert data["centerline_point_count"] == 2
    assert data["gps_sample_count"] == 2
    assert data["session_count"] == 2

    assert len(data["points"]) == 2

    point_0 = data["points"][0]

    assert point_0["survey_index"] == 0
    assert point_0["longitude"] == 24.001000
    assert point_0["latitude"] == 54.001000
    assert point_0["elevation"] == 176.42

    assert point_0["match"]["gps_longitude"] == 24.001001
    assert point_0["match"]["gps_latitude"] == 54.001001
    assert point_0["match"]["gps_elevation"] == 176.42
    assert point_0["match"]["session_index"] == 0
    assert point_0["match"]["distance_metres"] == 0.13

    point_1 = data["points"][1]

    assert point_1["survey_index"] == 1
    assert point_1["elevation"] == 177.31

    assert point_1["match"]["session_index"] == 1
    assert point_1["match"]["distance_metres"] == 0.17
