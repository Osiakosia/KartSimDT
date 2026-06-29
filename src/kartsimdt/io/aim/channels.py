"""
channels.py

KartSimDT AIM Import Module

Channel registry for AIM telemetry.
"""

from __future__ import annotations


class AimChannelRegistry:
    """
    Registry of supported AIM telemetry channels.
    """

    CHANNELS: dict[str, str] = {}

    @classmethod
    def has_channel(cls, channel_name: str) -> bool:
        """
        Check whether a channel is supported.
        """
        return channel_name in cls.CHANNELS

    @classmethod
    def get_channel_name(cls, channel_name: str) -> str:
        """
        Return the normalized KartSimDT channel name.
        """
        return cls.CHANNELS[channel_name]
