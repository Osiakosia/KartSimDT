"""
run_aim_smoke_test.py

Smoke test for AIM telemetry import.
"""

from pathlib import Path

from kartsimdt.io.aim.parser import AimTelemetryParser


def main() -> None:

    PROJECT_ROOT = Path(__file__).resolve().parents[4]

    csv_file = PROJECT_ROOT / "data" / "tracks" / "Aukštadvaris" / "aim" / "session.csv"

    parser = AimTelemetryParser()

    session = parser.parse(csv_file)

    print("\n========== AIM SMOKE TEST ==========")

    print(f"Session : {session.metadata.session_name}")

    print(f"Channels: {session.channel_count()}")

    print("\nAvailable channels:")

    for name in session.channels.names():
        print(f"  {name}")

    latitude = session.channels.get("gps_latitude")
    longitude = session.channels.get("gps_longitude")
    altitude = session.channels.get("gps_altitude")

    print("\nGPS:")

    print(f"Latitude : {'OK' if latitude else 'MISSING'}")
    print(f"Longitude: {'OK' if longitude else 'MISSING'}")
    print(f"Altitude : {'OK' if altitude else 'MISSING'}")

    if altitude:

        print()

        print(f"Samples : {altitude.count()}")

        print(f"Min Alt : {altitude.minimum()}")

        print(f"Max Alt : {altitude.maximum()}")

    print("\n====================================")


if __name__ == "__main__":
    main()
