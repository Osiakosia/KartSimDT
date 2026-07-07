from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class SessionMetadata:
    """
    Descriptive information about a telemetry session.

    This object is independent of the telemetry source format.
    """

    session_name: str = ""

    track_name: str = ""

    driver_name: str = ""

    vehicle_name: str = ""

    logger_name: str = ""

    recording_date: datetime | None = None

    notes: str = ""

    extra_metadata: dict[str, str] = field(default_factory=dict)

    @property
    def has_driver(self) -> bool:
        return bool(self.driver_name)

    @property
    def has_track(self) -> bool:
        return bool(self.track_name)

    @property
    def has_vehicle(self) -> bool:
        return bool(self.vehicle_name)

    @property
    def has_recording_date(self) -> bool:
        return self.recording_date is not None
