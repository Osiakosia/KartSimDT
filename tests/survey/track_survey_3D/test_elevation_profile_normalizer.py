from kartsimdt.survey.track_survey_3d.elevation_profile import (
    ElevationProfile,
    ElevationProfilePoint,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_normalizer import (
    ElevationProfileNormalizer,
)


def test_normalize_removes_mean_elevation() -> None:
    profile = ElevationProfile(
        points=(
            ElevationProfilePoint(
                survey_index=0,
                elevation=100.0,
                measurement_count=1,
            ),
            ElevationProfilePoint(
                survey_index=1,
                elevation=102.0,
                measurement_count=1,
            ),
            ElevationProfilePoint(
                survey_index=2,
                elevation=104.0,
                measurement_count=1,
            ),
        ),
    )

    normalized = ElevationProfileNormalizer().normalize(
        profile,
    )

    assert [point.elevation for point in normalized.points] == [
        -2.0,
        0.0,
        2.0,
    ]


def test_normalization_preserves_survey_index() -> None:
    profile = ElevationProfile(
        points=(
            ElevationProfilePoint(
                survey_index=10,
                elevation=150.0,
                measurement_count=45,
            ),
            ElevationProfilePoint(
                survey_index=20,
                elevation=152.0,
                measurement_count=45,
            ),
        ),
    )

    normalized = ElevationProfileNormalizer().normalize(
        profile,
    )

    assert [point.survey_index for point in normalized.points] == [10, 20]


def test_normalization_preserves_measurement_count() -> None:
    profile = ElevationProfile(
        points=(
            ElevationProfilePoint(
                survey_index=0,
                elevation=150.0,
                measurement_count=45,
            ),
            ElevationProfilePoint(
                survey_index=1,
                elevation=152.0,
                measurement_count=45,
            ),
        ),
    )

    normalized = ElevationProfileNormalizer().normalize(
        profile,
    )

    assert [point.measurement_count for point in normalized.points] == [45, 45]


def test_normalize_empty_profile() -> None:
    profile = ElevationProfile(
        points=(),
    )

    normalized = ElevationProfileNormalizer().normalize(
        profile,
    )

    assert normalized.points == ()
