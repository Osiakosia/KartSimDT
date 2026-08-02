from __future__ import annotations

from . import operators, panels, preferences, properties
from .services import calibration_loader


def register() -> None:
    properties.register()
    operators.register()
    panels.register()
    preferences.register()

    calibration_loader.register()


def unregister() -> None:
    calibration_loader.unregister()

    panels.unregister()
    operators.unregister()
    properties.unregister()
    preferences.unregister()
