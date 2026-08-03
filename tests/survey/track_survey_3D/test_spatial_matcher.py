"""
test_spatial_matcher.py

Tests for SpatialMatcher.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.metadata import SurveyMetadata
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.gps_dataset import (
    GpsElevationDataset,
)
from kartsimdt.survey.track_survey_3d.gps_dataset_builder import (
    GpsDatasetBuilder,
)
from kartsimdt.survey.track_survey_3d.gps_sample import (
    GpsElevationSample,
)
from kartsimdt.survey.track_survey_3d.spatial_matcher import (
    SpatialMatcher,
)
from kartsimdt.telemetry.channel import TelemetryChannel
from kartsimdt.telemetry.session import TelemetrySession


def test_match_single_point() -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=24.000000,
                    latitude=54.000000,
                ),
            ],
        ),
    )

    dataset = GpsElevationDataset()

    dataset.add(
        GpsElevationSample(
            latitude=54.000000,
            longitude=24.000000,
            elevation=176.5,
            session_index=0,
        )
    )

    matcher = SpatialMatcher()

    result = matcher.match(
        survey,
        dataset,
    )

    assert result.count() == 1

    match = result.matches[0]

    assert match.survey_index == 0

    assert match.gps_sample.session_index == 0

    assert match.gps_sample.latitude == 54.000000

    assert match.gps_sample.longitude == 24.000000

    assert match.gps_sample.elevation == 176.5


def test_match_nearest_sample() -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=24.0010,
                    latitude=54.0010,
                ),
            ],
        ),
    )

    dataset = GpsElevationDataset()

    dataset.add(
        GpsElevationSample(
            latitude=54.0000,
            longitude=24.0000,
            elevation=100.0,
            session_index=0,
        )
    )

    dataset.add(
        GpsElevationSample(
            latitude=54.0010,
            longitude=24.0010,
            elevation=200.0,
            session_index=0,
        )
    )

    dataset.add(
        GpsElevationSample(
            latitude=54.0050,
            longitude=24.0050,
            elevation=300.0,
            session_index=0,
        )
    )

    matcher = SpatialMatcher()

    result = matcher.match(
        survey,
        dataset,
    )

    match = result.matches[0]

    print("\n========== MATCH RESULT ==========")
    print(
        f"Survey point : ({match.survey_longitude:.6f}, "
        f"{match.survey_latitude:.6f})"
    )
    print(
        f"Matched GPS  : ({match.gps_sample.longitude:.6f}, "
        f"{match.gps_sample.latitude:.6f})"
    )
    print(f"Elevation    : {match.gps_sample.elevation}")
    print(f"Session      : {match.gps_sample.session_index}")
    print(f"Distance     : {match.distance_metres}")
    print("==================================")

    assert result.count() == 1

    assert match.gps_sample.elevation == 200.0

    assert match.gps_sample.session_index == 0


def test_match_multiple_points() -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(longitude=24.0000, latitude=54.0000),
                Point(longitude=24.0020, latitude=54.0020),
                Point(longitude=24.0040, latitude=54.0040),
            ],
        ),
    )

    dataset = GpsElevationDataset()

    dataset.add(
        GpsElevationSample(
            latitude=54.0000,
            longitude=24.0000,
            elevation=100.0,
            session_index=0,
        )
    )

    dataset.add(
        GpsElevationSample(
            latitude=54.0020,
            longitude=24.0020,
            elevation=200.0,
            session_index=0,
        )
    )

    dataset.add(
        GpsElevationSample(
            latitude=54.0040,
            longitude=24.0040,
            elevation=300.0,
            session_index=0,
        )
    )

    matcher = SpatialMatcher()

    result = matcher.match(
        survey,
        dataset,
    )

    print("\n============= MATCHES =============")

    for match in result.matches:
        print(
            f"Survey[{match.survey_index}] "
            f"-> Elevation={match.gps_sample.elevation:.1f} "
            f"Session={match.gps_sample.session_index}"
        )

    print("==================================")

    assert result.count() == 3

    assert result.matches[0].gps_sample.elevation == 100.0
    assert result.matches[1].gps_sample.elevation == 200.0
    assert result.matches[2].gps_sample.elevation == 300.0

    assert result.matches[0].gps_sample.session_index == 0
    assert result.matches[1].gps_sample.session_index == 0
    assert result.matches[2].gps_sample.session_index == 0


def test_match_multiple_sessions() -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=24.0100,
                    latitude=54.0100,
                ),
            ],
        ),
    )

    session0 = TelemetrySession()

    session0.channels.add(
        TelemetryChannel(
            name="gps_latitude",
            unit="deg",
            samples=[
                54.0000,
                54.0010,
            ],
        )
    )

    session0.channels.add(
        TelemetryChannel(
            name="gps_longitude",
            unit="deg",
            samples=[
                24.0000,
                24.0010,
            ],
        )
    )

    session0.channels.add(
        TelemetryChannel(
            name="gps_altitude",
            unit="m",
            samples=[
                100.0,
                110.0,
            ],
        )
    )

    session1 = TelemetrySession()

    session1.channels.add(
        TelemetryChannel(
            name="gps_latitude",
            unit="deg",
            samples=[
                54.0100,
                54.0110,
            ],
        )
    )

    session1.channels.add(
        TelemetryChannel(
            name="gps_longitude",
            unit="deg",
            samples=[
                24.0100,
                24.0110,
            ],
        )
    )

    session1.channels.add(
        TelemetryChannel(
            name="gps_altitude",
            unit="m",
            samples=[
                200.0,
                210.0,
            ],
        )
    )

    dataset = GpsDatasetBuilder().build(
        [
            session0,
            session1,
        ]
    )

    matcher = SpatialMatcher()

    result = matcher.match(
        survey,
        dataset,
    )

    match = result.matches[0]

    print("\n========== MULTI SESSION ==========")
    print(f"Matched elevation : {match.gps_sample.elevation}")
    print(f"Session index     : {match.gps_sample.session_index}")
    print("===================================")

    assert result.count() == 1

    assert match.gps_sample.elevation == 200.0

    assert match.gps_sample.session_index == 1
