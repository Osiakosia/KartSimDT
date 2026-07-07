"""
inspect_laps.py

Inspect lap-related information contained in an AIM telemetry file.
"""

from pathlib import Path

from kartsimdt.io.aim.reader import AimCsvReader


def main() -> None:
    """
    Display all lap-related information from an AIM file.
    """

    file_path = Path("tests/data/aim/rotena_sample.csv")

    reader = AimCsvReader()
    raw = reader.read(file_path)

    print("\nLap-related Metadata\n")
    print("-" * 60)

    lap_keywords = (
        "Lap",
        "Segment",
        "Beacon",
        "Split",
        "Sector",
        "Time",
        "Duration",
    )

    found = False

    for key, value in raw.metadata.items():

        if any(keyword.lower() in key.lower() for keyword in lap_keywords):
            print(f"{key:<25}: {value}")
            found = True

    if not found:
        print("No lap-related metadata found.")

    print("\nTelemetry Channels\n")
    print("-" * 60)

    for index, (name, unit) in enumerate(
        zip(raw.channel_names, raw.channel_units, strict=True),
        start=1,
    ):
        print(f"{index:2d}. {name:<30} [{unit}]")

    print("\nSample Count\n")
    print("-" * 60)

    print(f"Samples : {len(raw.samples)}")


if __name__ == "__main__":
    main()
