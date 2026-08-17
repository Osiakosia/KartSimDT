"""
Run Centerline JSON exporter.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from kartsimdt.io.exporters.centerline_json_exporter import (
    CenterlineJsonExporter,
)
from kartsimdt.survey.track_survey.mapper import (
    TrackSurveyMapper,
)
from kartsimdt.survey.track_survey.reader import (
    TrackSurveyKmlReader,
)
from kartsimdt.survey.track_survey.validator import (
    TrackSurveyValidator,
)
from kartsimdt.track import TrackResolver
from kartsimdt.visualization.geometry.centerline_mapper import (
    CenterlineGeometryMapper,
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]

TRACKS_ROOT = PROJECT_ROOT / "data" / "tracks"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Export track centerline to KartSimDT JSON.",
    )

    parser.add_argument(
        "--track",
        required=True,
        help="Track name from data/tracks.",
    )

    return parser.parse_args()


def main() -> None:
    """
    Run Centerline JSON exporter.
    """

    args = parse_args()

    resolver = TrackResolver(
        tracks_root=TRACKS_ROOT,
    )

    track = resolver.resolve(
        args.track,
    )

    reader = TrackSurveyKmlReader()
    validator = TrackSurveyValidator()
    survey_mapper = TrackSurveyMapper()

    raw = reader.read(
        track.centerline_kml,
    )

    validator.validate(
        raw,
    )

    session = survey_mapper.map(
        raw,
    )

    geometry_mapper = CenterlineGeometryMapper()

    geometry = geometry_mapper.map(
        session,
    )

    exporter = CenterlineJsonExporter()

    exporter.export(
        geometry=geometry,
        output_file=track.centerline_json,
    )


if __name__ == "__main__":
    main()
