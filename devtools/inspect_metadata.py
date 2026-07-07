"""
inspect_metadata.py

Inspect mapped SessionMetadata from an AIM telemetry file.
"""

from pathlib import Path

from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.reader import AimCsvReader


def main() -> None:
    """
    Read an AIM file and display mapped session metadata.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    mapper = AimMapper()
    metadata = mapper._map_metadata(raw)

    print("\nSession Metadata\n")
    print("-" * 50)

    print(f"Session : {metadata.session_name}")
    print(f"Track   : {metadata.track_name}")
    print(f"Driver  : {metadata.driver_name}")
    print(f"Vehicle : {metadata.vehicle_name}")
    print(f"Logger  : {metadata.logger_name}")
    print(f"Date    : {metadata.recording_date}")
    print(f"Notes   : {metadata.notes}")

    print("\nExtra Metadata\n")
    print("-" * 50)

    for key, value in metadata.extra_metadata.items():
        print(f"{key:<20} : {value}")


if __name__ == "__main__":
    main()
