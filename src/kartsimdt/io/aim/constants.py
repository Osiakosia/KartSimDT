"""
constants.py

KartSimDT AIM Import Module

Constants used by the AIM import subsystem.
"""

from __future__ import annotations

SUPPORTED_FILE_EXTENSIONS = (".csv",)

SUPPORTED_ENCODINGS = (
    "utf-8",
    "utf-8-sig",
    "cp1252",
)

SUPPORTED_DELIMITERS = (
    ",",
    ";",
)

DEFAULT_ENCODING = "utf-8"

DEFAULT_TIME_CHANNEL = "Time"

SUPPORTED_AIM_VERSIONS: tuple[str, ...] = ()
