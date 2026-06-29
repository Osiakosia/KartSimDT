"""
channels.py

KartSimDT Telemetry Module

Defines the ChannelCollection domain object representing
a collection of telemetry channels.
"""

from __future__ import annotations

from collections.abc import ItemsView, Iterator
from dataclasses import dataclass, field

from .channel import TelemetryChannel


@dataclass(slots=True)
class ChannelCollection:
    """
    Represents a collection of telemetry channels.

    Provides convenient methods for managing telemetry channels
    independently of the telemetry source.
    """

    channels: dict[str, TelemetryChannel] = field(default_factory=dict)

    def add(self, channel: TelemetryChannel) -> None:
        """Add a telemetry channel."""
        self.channels[channel.name] = channel

    def remove(self, name: str) -> None:
        """Remove a telemetry channel."""
        self.channels.pop(name, None)

    def clear(self) -> None:
        """Remove all telemetry channels."""
        self.channels.clear()

    def count(self) -> int:
        """Return the number of channels."""
        return len(self.channels)

    def is_empty(self) -> bool:
        """Return True if no channels exist."""
        return len(self.channels) == 0

    def exists(self, name: str) -> bool:
        """Check whether a channel exists."""
        return name in self.channels

    def get(self, name: str) -> TelemetryChannel | None:
        """Return a channel by name."""
        return self.channels.get(name)

    def names(self) -> list[str]:
        """Return channel names."""
        return list(self.channels.keys())

    def values(self) -> list[TelemetryChannel]:
        """Return all channel objects."""
        return list(self.channels.values())

    def items(self) -> ItemsView[str, TelemetryChannel]:
        """Return channel name/object pairs."""
        return self.channels.items()

    def first(self) -> TelemetryChannel | None:
        """Return the first channel."""
        if self.is_empty():
            return None

        return next(iter(self.channels.values()))

    def last(self) -> TelemetryChannel | None:
        """Return the last channel."""
        if self.is_empty():
            return None

        return list(self.channels.values())[-1]

    def __len__(self) -> int:
        """Return the number of channels."""
        return len(self.channels)

    def __iter__(self) -> Iterator[TelemetryChannel]:
        """Iterate over telemetry channels."""
        return iter(self.channels.values())

    def __getitem__(self, name: str) -> TelemetryChannel:
        """Return channel by name."""
        return self.channels[name]
