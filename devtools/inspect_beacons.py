"""
inspect_beacons.py

Development tool for inspecting AIM beacon markers.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.beacons import AimBeaconParser
from kartsimdt.io.aim.reader import AimCsvReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    """
    Inspect AIM beacon markers.
    """

    file_path = PROJECT_ROOT / "tests" / "data" / "aim" / "rotena_session.csv"

    reader = AimCsvReader()
    raw = reader.read(file_path)

    parser = AimBeaconParser()

    beacons = parser.parse(raw.metadata)

    print("\nBeacon Markers\n")
    print("-" * 40)

    for lap_number, beacon in enumerate(beacons, start=1):
        print(f"{lap_number:2d}: {beacon:.3f} s")


if __name__ == "__main__":
    main()
