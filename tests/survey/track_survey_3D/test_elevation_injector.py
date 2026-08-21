"""
test_elevation_injector.py

Tests for ElevationInjector.
"""

from __future__ import annotations

from kartsimdt.survey.track_survey.centerline import Centerline
from kartsimdt.survey.track_survey.metadata import SurveyMetadata
from kartsimdt.survey.track_survey.point import Point
from kartsimdt.survey.track_survey.session import TrackSurveySession
from kartsimdt.survey.track_survey_3d.elevation_injector import (
    ElevationInjector,
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


def test_inject_elevation() -> None:
    longitude = 24.001000
    latitude = 54.001000

    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=longitude,
                    latitude=latitude,
                    elevation=None,
                ),
            ],
        ),
    )

    gps_sample = GpsElevationSample(
        latitude=54.001001,
        longitude=24.001002,
        elevation=176.5,
        session_index=0,
    )

    matches = MatchedElevationDataset()

    matches.add(
        MatchedElevation(
            survey_index=0,
            survey_latitude=latitude,
            survey_longitude=longitude,
            gps_sample=gps_sample,
            distance_metres=0.25,
        )
    )

    point = survey.centerline.points[0]

    print("\n========== BEFORE INJECTION ==========")
    print(f"Longitude : {point.longitude:.6f}")
    print(f"Latitude  : {point.latitude:.6f}")
    print(f"Elevation : {point.elevation}")
    print("======================================")

    injector = ElevationInjector()

    injector.inject(
        survey,
        matches,
    )

    point = survey.centerline.points[0]

    print("\n========== AFTER INJECTION ===========")
    print(f"Longitude : {point.longitude:.6f}")
    print(f"Latitude  : {point.latitude:.6f}")
    print(f"Elevation : {point.elevation}")
    print("======================================")

    assert point.longitude == longitude
    assert point.latitude == latitude
    assert point.elevation == 176.5


def test_inject_multiple_elevations() -> None:
    survey = TrackSurveySession(
        metadata=SurveyMetadata(
            name="Test Track",
            description="",
        ),
        centerline=Centerline(
            points=[
                Point(
                    longitude=24.0000,
                    latitude=54.0000,
                    elevation=None,
                ),
                Point(
                    longitude=24.0010,
                    latitude=54.0010,
                    elevation=None,
                ),
                Point(
                    longitude=24.0020,
                    latitude=54.0020,
                    elevation=None,
                ),
            ],
        ),
    )

    matches = MatchedElevationDataset()

    elevations = [
        176.2,
        177.4,
        175.8,
    ]

    for index, elevation in enumerate(elevations):
        point = survey.centerline.points[index]

        matches.add(
            MatchedElevation(
                survey_index=index,
                survey_latitude=point.latitude,
                survey_longitude=point.longitude,
                gps_sample=GpsElevationSample(
                    latitude=point.latitude,
                    longitude=point.longitude,
                    elevation=elevation,
                    session_index=0,
                ),
                distance_metres=0.0,
            )
        )

    injector = ElevationInjector()

    injector.inject(
        survey,
        matches,
    )

    print("\n========== ELEVATION PROFILE ==========")

    for index, point in enumerate(survey.centerline.points):
        print(
            f"Point[{index}] "
            f"lon={point.longitude:.6f} "
            f"lat={point.latitude:.6f} "
            f"elevation={point.elevation:.2f} m"
        )

    print("=======================================")

    assert survey.centerline.points[0].elevation == 176.2
    assert survey.centerline.points[1].elevation == 177.4
    assert survey.centerline.points[2].elevation == 175.8

    assert survey.centerline.points[0].longitude == 24.0000
    assert survey.centerline.points[1].longitude == 24.0010
    assert survey.centerline.points[2].longitude == 24.0020

    assert survey.centerline.points[0].latitude == 54.0000
    assert survey.centerline.points[1].latitude == 54.0010
    assert survey.centerline.points[2].latitude == 54.0020
