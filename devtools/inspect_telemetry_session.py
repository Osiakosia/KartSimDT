"""
inspect_telemetry_session.py

KartSimDT Engineering Inspector

Displays the complete TelemetrySession transformation pipeline.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.beacons import AimBeaconParser
from kartsimdt.io.aim.mapper import AimMapper
from kartsimdt.io.aim.reader import AimCsvReader
from kartsimdt.io.aim.segment_times import AimSegmentTimeParser
from kartsimdt.io.aim.validator import AimValidator

# ============================================================================
# Project Paths
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

TEST_DATA = PROJECT_ROOT / "tests" / "data" / "aim"

DATASETS = {
    "sample": TEST_DATA / "rotena_sample.csv",
    "session": TEST_DATA / "rotena_session.csv",
}

DATASET = DATASETS["session"]


# ============================================================================
# Helpers
# ============================================================================


def separator(title: str) -> None:
    """Print section separator."""
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    reader = AimCsvReader()
    validator = AimValidator()
    mapper = AimMapper()

    raw = reader.read(DATASET)
    validator.validate(raw)
    session = mapper.map(raw)

    separator("KartSimDT Engineering Inspector")
    print("Telemetry Session")

    separator("Reference Dataset")
    print(f"File       : {DATASET.name}")
    print(f"Rows       : {len(raw.samples)}")
    print(f"Channels   : {len(raw.channel_names)}")

    separator("Raw AIM Metadata")
    for key, value in raw.metadata.items():
        print(f"{key:20}: {value}")

    separator("Raw AIM Channels")
    for name, unit in zip(
        raw.channel_names,
        raw.channel_units,
        strict=True,
    ):
        print(f"{name:30} {unit}")

    separator("Raw AIM Samples")

    print("Rows :", len(raw.samples))
    print("Cols :", len(raw.samples.columns))

    print("\nFirst sample")
    print(raw.samples.iloc[0])

    print("\nLast sample")
    print(raw.samples.iloc[-1])

    separator("Beacon Parser")

    beacons = AimBeaconParser().parse(raw.metadata)

    for i, beacon in enumerate(beacons, start=1):
        print(f"Lap {i:2d} : {beacon:.3f}")

    separator("Segment Parser")

    segments = AimSegmentTimeParser().parse(raw.metadata)

    for i, segment in enumerate(segments, start=1):
        print(f"Lap {i:2d} : {segment:.3f}")

    separator("Mapped Metadata")

    metadata = session.metadata

    print(f"Session : {metadata.session_name}")
    print(f"Track   : {metadata.track_name}")
    print(f"Driver  : {metadata.driver_name}")
    print(f"Vehicle : {metadata.vehicle_name}")
    print(f"Logger  : {metadata.logger_name}")

    separator("Mapped Channels")

    print(f"Total channels : {session.channels.count()}")

    for channel in session.channels:
        print(f"{channel.name:25}" f"{channel.unit:8}" f"samples={channel.count()}")

    separator("Lap Collection")

    print(f"{'Lap':>4} " f"{'Start':>10} " f"{'Finish':>10} " f"{'Duration':>10}")

    for lap in session.laps:
        print(
            f"{lap.number:4d} "
            f"{lap.start_time:10.3f} "
            f"{lap.end_time:10.3f} "
            f"{lap.duration:10.3f}"
        )

    separator("Telemetry Session")

    print("Metadata : OK")
    print(f"Channels : {session.channels.count()}")
    print(f"Laps     : {session.laps.count()}")

    durations = [lap.duration for lap in session.laps]

    fastest = min(durations)
    slowest = max(durations)

    fastest_lap = durations.index(fastest) + 1
    slowest_lap = durations.index(slowest) + 1

    print(f"Fastest Lap : #{fastest_lap} ({fastest:.3f} s)")
    print(f"Slowest Lap : #{slowest_lap} ({slowest:.3f} s)")
    print(f"Duration    : {durations[-1] + session.laps[-1].start_time:.3f} s")

    separator("Validation Summary")

    print("AimCsvReader      PASS")
    print("AimValidator      PASS")
    print("Metadata Mapper   PASS")
    print("Channel Mapper    PASS")
    print("Beacon Parser     PASS")
    print("Segment Parser    PASS")
    print("Lap Mapper        PASS")
    print("TelemetrySession  PASS")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
