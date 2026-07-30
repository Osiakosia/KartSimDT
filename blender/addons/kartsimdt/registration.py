from __future__ import annotations

from . import operators, panels, properties


def register() -> None:
    properties.register()
    operators.register()
    panels.register()


def unregister() -> None:
    panels.unregister()
    operators.unregister()
    properties.unregister()
