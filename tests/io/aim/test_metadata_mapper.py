from pathlib import Path

from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.reader import AimCsvReader
from kartsimdt.telemetry.metadata import SessionMetadata


def test_map_metadata_returns_session_metadata() -> None:
    """
    Verify that metadata mapping returns a SessionMetadata object.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    metadata = mapper._map_metadata(raw)

    assert isinstance(metadata, SessionMetadata)


def test_map_metadata_maps_core_fields() -> None:
    """
    Verify that core session metadata is mapped correctly.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    metadata = mapper._map_metadata(raw)

    assert metadata.session_name == "Rotena"
    assert metadata.track_name == "Rotena"
    assert metadata.driver_name == "Jokūbas Kupstas"
    assert metadata.vehicle_name == "kartingas"


def test_map_metadata_preserves_extra_metadata() -> None:
    """
    Verify that unmapped AIM metadata is preserved.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    metadata = mapper._map_metadata(raw)

    assert "Format" in metadata.extra_metadata
    assert metadata.extra_metadata["Format"] == "AiM CSV File"

    assert "Sample Rate" in metadata.extra_metadata


def test_map_metadata_has_driver() -> None:
    """
    Verify SessionMetadata helper properties.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()

    metadata = mapper._map_metadata(raw)

    assert metadata.has_driver
    assert metadata.has_track
    assert metadata.has_vehicle
