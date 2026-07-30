"""
Run Centerline JSON exporter.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.exporters.centerline_json_exporter import (
    CenterlineJsonExporter,
)
from kartsimdt.survey.track_survey.mapper import (
    TrackSurveyMapper,
)
from kartsimdt.survey.track_survey.reader import TrackSurveyKmlReader
from kartsimdt.survey.track_survey.validator import (
    TrackSurveyValidator,
)
from kartsimdt.visualization.geometry.centerline_mapper import (
    CenterlineGeometryMapper,
)

ROOT = Path(__file__).resolve().parents[4]

DATASET = ROOT / "data" / "tracks" / "Aukštadvaris" / "walkthrough" / "centerline.kml"

OUTPUT = ROOT / "data" / "tracks" / "Aukštadvaris" / "walkthrough" / "centerline.json"


def main() -> None:
    """
    Run Centerline JSON exporter.
    """

    reader = TrackSurveyKmlReader()
    validator = TrackSurveyValidator()
    survey_mapper = TrackSurveyMapper()

    raw = reader.read(DATASET)
    validator.validate(raw)

    session = survey_mapper.map(raw)

    geometry_mapper = CenterlineGeometryMapper()

    geometry = geometry_mapper.map(session)

    exporter = CenterlineJsonExporter()

    exporter.export(
        geometry=geometry,
        output_file=OUTPUT,
    )


if __name__ == "__main__":
    main()
