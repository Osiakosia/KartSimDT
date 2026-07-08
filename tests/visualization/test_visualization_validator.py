"""
Unit tests for BlenderCurveValidator.
"""

from kartsimdt.visualization.blender.curve import BlenderCurve
from kartsimdt.visualization.blender.validator import (
    BlenderCurveValidator,
)


def test_validator_accepts_valid_curve() -> None:
    """
    Verify that a valid BlenderCurve passes validation.
    """

    curve = BlenderCurve(
        name="Test Curve",
        points=[
            (0.0, 0.0, 0.0),
            (1.0, 1.0, 0.0),
        ],
    )

    validator = BlenderCurveValidator()

    validator.validate(curve)
