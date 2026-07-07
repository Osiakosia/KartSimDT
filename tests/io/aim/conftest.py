"""
conftest.py

Shared pytest fixtures for the AIM import module.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from kartsimdt.io.aim.raw import AimRawData
from kartsimdt.io.aim.reader import AimCsvReader
from kartsimdt.io.aim.validator import AimValidator


@pytest.fixture(scope="session")
def reference_csv() -> Path:
    """
    Return the path to the Rotena reference AIM dataset.
    """
    return Path("tests/data/aim/rotena_sample.csv")


@pytest.fixture(scope="session")
def raw_data(reference_csv: Path) -> AimRawData:
    """
    Read the reference AIM dataset.
    """
    reader = AimCsvReader()
    return reader.read(reference_csv)


@pytest.fixture(scope="session")
def validated_raw(raw_data: AimRawData) -> AimRawData:
    """
    Validate the reference AIM dataset.
    """
    validator = AimValidator()
    validator.validate(raw_data)

    return raw_data


@pytest.fixture(scope="session")
def session_csv() -> Path:
    """
    Return the full Rotena AIM session dataset.
    """
    return Path("tests/data/aim/rotena_session.csv")


@pytest.fixture(scope="session")
def session_raw(session_csv: Path) -> AimRawData:
    reader = AimCsvReader()
    return reader.read(session_csv)


@pytest.fixture(scope="session")
def validated_session(session_raw: AimRawData) -> AimRawData:
    validator = AimValidator()
    validator.validate(session_raw)
    return session_raw
