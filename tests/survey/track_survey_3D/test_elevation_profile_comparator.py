import pytest

from kartsimdt.survey.track_survey_3d.elevation_profile import (
    ElevationProfile,
    ElevationProfilePoint,
)
from kartsimdt.survey.track_survey_3d.elevation_profile_comparator import (
    ElevationProfileComparator,
)


def make_profile(
    elevations: tuple[float, ...],
) -> ElevationProfile:
    return ElevationProfile(
        points=tuple(
            ElevationProfilePoint(
                survey_index=index,
                elevation=elevation,
                measurement_count=1,
            )
            for index, elevation in enumerate(elevations)
        ),
    )


def test_compare_identical_profiles() -> None:
    profile = make_profile((0.0, 1.0, 2.0, 1.0, 0.0))

    result = ElevationProfileComparator().compare(
        reference=profile,
        candidate=profile,
    )

    assert result.point_count == 5
    assert result.mae == pytest.approx(0.0)
    assert result.rmse == pytest.approx(0.0)
    assert result.max_absolute_error == pytest.approx(0.0)
    assert result.correlation == pytest.approx(1.0)


def test_compare_profiles_calculates_errors() -> None:
    reference = make_profile((0.0, 2.0, 4.0))

    candidate = make_profile((1.0, 1.0, 3.0))

    result = ElevationProfileComparator().compare(
        reference=reference,
        candidate=candidate,
    )

    assert result.point_count == 3

    # Errors: -1, +1, +1
    assert result.mae == pytest.approx(1.0)

    assert result.rmse == pytest.approx(1.0)

    assert result.max_absolute_error == pytest.approx(1.0)


def test_compare_profiles_calculates_correlation() -> None:
    reference = make_profile((-2.0, 0.0, 2.0))

    candidate = make_profile((-1.0, 0.0, 1.0))

    result = ElevationProfileComparator().compare(
        reference=reference,
        candidate=candidate,
    )

    assert result.correlation == pytest.approx(1.0)


def test_compare_rejects_different_point_counts() -> None:
    reference = make_profile((0.0, 1.0, 2.0))

    candidate = make_profile((0.0, 1.0))

    with pytest.raises(ValueError):
        ElevationProfileComparator().compare(
            reference=reference,
            candidate=candidate,
        )


def test_compare_rejects_different_survey_indices() -> None:
    reference = make_profile((0.0, 1.0, 2.0))

    candidate = ElevationProfile(
        points=(
            ElevationProfilePoint(
                survey_index=0,
                elevation=0.0,
                measurement_count=1,
            ),
            ElevationProfilePoint(
                survey_index=5,
                elevation=1.0,
                measurement_count=1,
            ),
            ElevationProfilePoint(
                survey_index=2,
                elevation=2.0,
                measurement_count=1,
            ),
        ),
    )

    with pytest.raises(ValueError):
        ElevationProfileComparator().compare(
            reference=reference,
            candidate=candidate,
        )


def test_compare_rejects_empty_profile() -> None:
    empty = ElevationProfile(
        points=(),
    )

    profile = make_profile((0.0, 1.0, 2.0))

    with pytest.raises(ValueError):
        ElevationProfileComparator().compare(
            reference=empty,
            candidate=profile,
        )
