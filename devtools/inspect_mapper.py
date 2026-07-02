"""
inspect_mapper.py

Inspect AIM channel mapping into the KartSimDT telemetry model.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.reader import AimCsvReader


def main() -> None:
    """
    Display mapped telemetry channels.
    """

    reader = AimCsvReader()
    mapper = AimMapper()

    file_path = Path("tests/data/aim/rotena_sample.csv")

    raw = reader.read(file_path)

    channels = mapper._map_channels(raw)

    print()
    print(f"{'Channel':30}" f"{'Unit':8}" f"{'Samples':>10}")
    print("-" * 52)

    for channel in channels:
        print(f"{channel.name:30}" f"{channel.unit:8}" f"{channel.count():>10}")


if __name__ == "__main__":
    main()
