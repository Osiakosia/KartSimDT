"""
Comparison of elevation profiles.

The comparator expects two source-neutral ElevationProfile objects
with identical survey indices and calculates:

- MAE
- RMSE
- maximum absolute error
- Pearson correlation
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from kartsimdt.survey.track_survey_3d.elevation_profile import (
    ElevationProfile,
)


@dataclass(frozen=True, slots=True)
class ElevationProfileComparison:
    """Statistical comparison result for two elevation profiles."""

    point_count: int
    mae: float
    rmse: float
    max_absolute_error: float
    correlation: float


class ElevationProfileComparator:
    """Compare two source-neutral elevation profiles."""

    def compare(
        self,
        reference: ElevationProfile,
        candidate: ElevationProfile,
    ) -> ElevationProfileComparison:
        """Compare two elevation profiles."""

        self._validate_profiles(
            reference,
            candidate,
        )

        reference_values = [point.elevation for point in reference.points]

        candidate_values = [point.elevation for point in candidate.points]

        errors = [
            reference_value - candidate_value
            for reference_value, candidate_value in zip(
                reference_values,
                candidate_values,
                strict=True,
            )
        ]

        absolute_errors = [abs(error) for error in errors]

        squared_errors = [error * error for error in errors]

        point_count = len(errors)

        mae = sum(absolute_errors) / point_count

        rmse = sqrt(sum(squared_errors) / point_count)

        max_absolute_error = max(absolute_errors)

        correlation = self._pearson_correlation(
            reference_values,
            candidate_values,
        )

        return ElevationProfileComparison(
            point_count=point_count,
            mae=mae,
            rmse=rmse,
            max_absolute_error=max_absolute_error,
            correlation=correlation,
        )

    @staticmethod
    def _validate_profiles(
        reference: ElevationProfile,
        candidate: ElevationProfile,
    ) -> None:
        """Validate that profiles can be compared safely."""

        if not reference.points:
            raise ValueError("Reference elevation profile is empty.")

        if not candidate.points:
            raise ValueError("Candidate elevation profile is empty.")

        if len(reference.points) != len(candidate.points):
            raise ValueError(
                "Elevation profiles must contain " "the same number of points."
            )

        reference_indices = [point.survey_index for point in reference.points]

        candidate_indices = [point.survey_index for point in candidate.points]

        if reference_indices != candidate_indices:
            raise ValueError(
                "Elevation profiles must contain "
                "the same survey indices in the "
                "same order."
            )

    @staticmethod
    def _pearson_correlation(
        reference: list[float],
        candidate: list[float],
    ) -> float:
        """Calculate Pearson correlation coefficient."""

        if len(reference) != len(candidate):
            raise ValueError("Profiles must have the same number " "of values.")

        if len(reference) < 2:
            raise ValueError("At least two points are required " "for correlation.")

        count = len(reference)

        reference_mean = sum(reference) / count
        candidate_mean = sum(candidate) / count

        reference_deviations = [value - reference_mean for value in reference]

        candidate_deviations = [value - candidate_mean for value in candidate]

        numerator = sum(
            reference_deviation * candidate_deviation
            for reference_deviation, candidate_deviation in zip(
                reference_deviations,
                candidate_deviations,
                strict=True,
            )
        )

        reference_sum_squares = sum(
            deviation * deviation for deviation in reference_deviations
        )

        candidate_sum_squares = sum(
            deviation * deviation for deviation in candidate_deviations
        )

        denominator = sqrt(reference_sum_squares * candidate_sum_squares)

        if denominator == 0.0:
            raise ValueError(
                "Pearson correlation is undefined " "for a constant elevation profile."
            )

        return numerator / denominator
