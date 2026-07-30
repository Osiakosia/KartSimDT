"""
Comparison result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ComparisonResult:
    """
    Centerline comparison result.
    """

    reference_points: int
    candidate_points: int

    mean_error: float
    max_error: float
    rmse: float
