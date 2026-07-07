"""
inspect_segment_times.py

Development tool for inspecting AIM segment times.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.io.aim.reader import AimCsvReader
from kartsimdt.io.aim.segment_times import AimSegmentTimeParser

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    """
    Inspect AIM lap segment times.
    """

    file_path = PROJECT_ROOT / "tests" / "data" / "aim" / "rotena_session.csv"

    reader = AimCsvReader()
    raw = reader.read(file_path)

    parser = AimSegmentTimeParser()

    lap_times = parser.parse(raw.metadata)

    print("\nSegment Times\n")
    print("-" * 40)

    for lap_number, lap_time in enumerate(
        lap_times,
        start=1,
    ):
        print(f"{lap_number:2d}: {lap_time:.3f} s")


if __name__ == "__main__":
    main()
