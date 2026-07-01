import pandas as pd
import pytest

from kartsimdt.io.aim.exceptions import InvalidAimFileError
from kartsimdt.io.aim.raw import AimRawData
from kartsimdt.io.aim.validator import AimValidator


def test_validate_empty_metadata() -> None:
    raw = AimRawData(
        metadata={},
        channel_names=[],
        channel_units=[],
        samples=pd.DataFrame(),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_empty_channel_names() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[],
        channel_units=["s"],
        samples=pd.DataFrame([[0.0]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_empty_channel_units() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time"],
        channel_units=[],
        samples=pd.DataFrame([[0.0]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_empty_samples() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time"],
        channel_units=["s"],
        samples=pd.DataFrame(),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_empty_samples() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time"],
        channel_units=["s"],
        samples=pd.DataFrame(),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_channel_count_mismatch() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time", "Speed"],
        channel_units=["s"],
        samples=pd.DataFrame([[0.0, 10.0]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_sample_column_mismatch() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time", "Speed"],
        channel_units=["s", "km/h"],
        samples=pd.DataFrame([[0.0]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_missing_time_channel() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["GPS Speed"],
        channel_units=["km/h"],
        samples=pd.DataFrame([[0.0]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_time_channel_exists() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.00, 0.0, 54.5, 24.5],
                [0.05, 1.0, 54.5, 24.5],
                [0.10, 2.0, 54.5, 24.5],
            ]
        ),
    )

    validator = AimValidator()

    validator.validate(raw)


def test_validate_time_not_starting_at_zero() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.05, 0.0, 54.5, 24.5],
                [0.05, 1.0, 54.5, 24.5],
                [0.10, 2.0, 54.5, 24.5],
            ]
        ),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_time_starts_at_zero() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.00, 0.0, 54.5, 24.5],
                [0.05, 1.0, 54.5, 24.5],
                [0.10, 2.0, 54.5, 24.5],
            ]
        ),
    )

    validator = AimValidator()

    validator.validate(raw)


def test_validate_non_monotonic_time() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.00],
                [0.10],
                [0.05],
            ]
        ),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_monotonic_time() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.00, 0.0, 54.5, 24.5],
                [0.05, 1.0, 54.5, 24.5],
                [0.10, 2.0, 54.5, 24.5],
            ]
        ),
    )

    validator = AimValidator()

    validator.validate(raw)


def test_validate_duplicate_timestamps() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=["Time"],
        channel_units=["s"],
        samples=pd.DataFrame(
            [
                [0.00],
                [0.05],
                [0.05],
            ]
        ),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_unique_timestamps() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame(
            [
                [0.00, 0.0, 54.5, 24.5],
                [0.05, 1.0, 54.5, 24.5],
                [0.10, 2.0, 54.5, 24.5],
            ]
        ),
    )

    validator = AimValidator()

    validator.validate(raw)


def test_validate_missing_gps_speed() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame([[0.0, 54.5, 24.5]]),
    )

    validator = AimValidator()

    with pytest.raises(InvalidAimFileError):
        validator.validate(raw)


def test_validate_gps_speed_exists() -> None:
    raw = AimRawData(
        metadata={"Format": "AiM CSV File"},
        channel_names=[
            "Time",
            "GPS Speed",
            "GPS Latitude",
            "GPS Longitude",
        ],
        channel_units=[
            "s",
            "km/h",
            "deg",
            "deg",
        ],
        samples=pd.DataFrame([[0.0, 10.0, 54.5, 24.5]]),
    )

    validator = AimValidator()

    validator.validate(raw)
