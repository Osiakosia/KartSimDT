"""
inspect_aim_channels.py

Inspect AIM channels from a reference CSV dataset.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.channels import AimChannelRegistry
from kartsimdt.io.aim.reader import AimCsvReader


def main() -> None:
    """
    Display all channels found in the reference AIM dataset.
    """
    reader = AimCsvReader()

    file_path = Path("tests/data/aim/rotena_sample.csv")

    raw = reader.read(file_path)

    print()
    print(f"{'AIM Channel':35} {'Unit':8} {'Mapped':8} {'KartSimDT Channel'}")
    print("-" * 80)

    for name, unit in zip(
        raw.channel_names,
        raw.channel_units,
        strict=True,
    ):
        supported = AimChannelRegistry.has_channel(name)

        if supported:
            mapped_name = AimChannelRegistry.get_channel_name(name)
        else:
            mapped_name = "-"

        print(
            f"{name:35} "
            f"{unit:8} "
            f"{'Yes' if supported else 'No':8} "
            f"{mapped_name}"
        )


if __name__ == "__main__":
    main()
