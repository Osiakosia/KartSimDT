"""
Elevation profile plotting.

Provides visual comparison of normalized elevation profiles
from different sources such as AIM telemetry and Google Earth.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from .elevation_profile import ElevationProfile


class ElevationProfilePlotter:
    """Plot and visually compare elevation profiles."""

    def plot_comparison(
        self,
        *,
        aim: ElevationProfile,
        google: ElevationProfile,
        output_path: Path | None = None,
        show: bool = False,
    ) -> None:
        """
        Plot normalized AIM and Google elevation profiles.

        Parameters
        ----------
        aim:
            Normalized AIM elevation profile.

        google:
            Normalized Google elevation profile.

        output_path:
            Optional path where the figure will be saved.

        show:
            If True, display the figure interactively.
        """

        self._validate_profiles(
            aim,
            google,
        )

        x = [point.survey_index for point in aim.points]

        aim_elevation = [point.elevation for point in aim.points]

        google_elevation = [point.elevation for point in google.points]

        difference = [
            aim_value - google_value
            for aim_value, google_value in zip(
                aim_elevation,
                google_elevation,
                strict=True,
            )
        ]

        fig, (
            ax_profile,
            ax_difference,
        ) = plt.subplots(
            2,
            1,
            figsize=(14, 8),
            sharex=True,
        )

        # -----------------------------------------------------
        # Elevation profiles
        # -----------------------------------------------------

        ax_profile.plot(
            x,
            aim_elevation,
            label="AIM",
            linewidth=1.5,
        )

        ax_profile.plot(
            x,
            google_elevation,
            label="Google Earth",
            linewidth=1.5,
        )

        ax_profile.set_title("KartSimDT — Normalized Elevation Profile")

        ax_profile.set_ylabel("Normalized elevation [m]")

        ax_profile.grid(
            True,
            alpha=0.3,
        )

        ax_profile.legend()

        # -----------------------------------------------------
        # Difference
        # -----------------------------------------------------

        ax_difference.plot(
            x,
            difference,
            label="AIM - Google",
            linewidth=1.2,
        )

        ax_difference.axhline(
            0.0,
            linewidth=1.0,
        )

        ax_difference.set_title("Elevation Difference")

        ax_difference.set_xlabel("Survey index")

        ax_difference.set_ylabel("Difference [m]")

        ax_difference.grid(
            True,
            alpha=0.3,
        )

        ax_difference.legend()

        fig.tight_layout()

        # -----------------------------------------------------
        # Save
        # -----------------------------------------------------

        if output_path is not None:
            output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            fig.savefig(
                output_path,
                dpi=150,
                bbox_inches="tight",
            )

        if show:
            plt.show()

        plt.close(fig)

    @staticmethod
    def _validate_profiles(
        aim: ElevationProfile,
        google: ElevationProfile,
    ) -> None:
        """Validate that profiles can be plotted together."""

        if not aim.points:
            raise ValueError("AIM elevation profile is empty.")

        if not google.points:
            raise ValueError("Google elevation profile is empty.")

        if len(aim.points) != len(google.points):
            raise ValueError(
                "AIM and Google elevation profiles "
                "must contain the same number of points."
            )

        aim_indices = [point.survey_index for point in aim.points]

        google_indices = [point.survey_index for point in google.points]

        if aim_indices != google_indices:
            raise ValueError(
                "AIM and Google elevation profiles "
                "must contain the same survey indices "
                "in the same order."
            )
