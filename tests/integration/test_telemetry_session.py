"""
Verify that a complete TelemetrySession can be created
from a real AIM session CSV file.
"""

from pathlib import Path

from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.reader import AimCsvReader
from kartsimdt.io.aim.validator import AimValidator
from kartsimdt.telemetry.session import TelemetrySession


def test_full_aim_import_pipeline() -> None:
    """
    Verify the complete AIM import pipeline from CSV
    to TelemetrySession.
    """

    file_path = Path("tests/data/aim/rotena_session.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    validator = AimValidator()
    validator.validate(raw)

    mapper = AimMapper()
    session = mapper.map(raw)

    assert isinstance(session, TelemetrySession)

    assert session.metadata.has_driver
    assert session.metadata.has_track
    assert session.metadata.has_vehicle

    assert session.metadata is not None
    assert session.channels is not None
    assert session.laps is not None

    assert len(session.channels) > 0
