"""
validator.py

Blender curve validator.
"""

from __future__ import annotations

import math

from .curve import BlenderCurve


class BlenderCurveValidator:
    """
    Validates a BlenderCurve.
    """

    def validate(
        self,
        curve: BlenderCurve,
    ) -> None:
        """
        Validate a BlenderCurve.
        """

        if not curve.name.strip():
            raise ValueError("Curve name cannot be empty.")

        if curve.count() < 2:
            raise ValueError(
                "A BlenderCurve must contain at least two points.",
            )

        for x, y, z in curve.points:

            if not math.isfinite(x):
                raise ValueError("Invalid X coordinate.")

            if not math.isfinite(y):
                raise ValueError("Invalid Y coordinate.")

            if not math.isfinite(z):
                raise ValueError("Invalid Z coordinate.")
