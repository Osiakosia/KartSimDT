from pathlib import Path

from kartsimdt.io.aim.reader import AimCsvReader


def main() -> None:
    reader = AimCsvReader()

    file_path = Path("tests/data/aim/rotena_sample.csv")

    raw = reader.read(file_path)

    print("\nMetadata:\n")

    for key, value in raw.metadata.items():
        print(f"{key}: {value}")

    print("\nChannel names:\n")

    for index, name in enumerate(raw.channel_names, start=1):
        print(f"{index:2d}. {name}")

    print("\nChannel units:\n")

    for index, unit in enumerate(raw.channel_units, start=1):
        print(f"{index:2d}. {unit}")

    print("\nSamples:\n")
    print(raw.samples.head())

    print(f"\nShape: {raw.samples.shape}")


if __name__ == "__main__":
    main()
