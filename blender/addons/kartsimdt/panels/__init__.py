"""
KartSimDT Panels Package

Responsibilities
----------------
- Register all panel modules.
- Unregister all panel modules.
"""

from __future__ import annotations

from . import panel


def register() -> None:
    panel.register()


def unregister() -> None:
    panel.unregister()
