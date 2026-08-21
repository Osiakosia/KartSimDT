"""
google_elevation_client.py

Client for retrieving terrain elevation from Google Elevation API.
"""

from __future__ import annotations

from dataclasses import dataclass

import requests

from kartsimdt.survey.track_survey.point import Point


@dataclass(slots=True)
class GoogleElevationPoint:
    """
    Google terrain elevation for one survey point.
    """

    latitude: float
    longitude: float
    elevation: float
    resolution: float | None = None


class GoogleElevationClient:
    """
    Retrieves Google terrain elevation for survey points.
    """

    BASE_URL = "https://maps.googleapis.com/maps/api/elevation/json"

    # Keep this configurable.
    DEFAULT_BATCH_SIZE = 100

    def __init__(
        self,
        api_key: str,
        timeout: float = 10.0,
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> None:
        if not api_key:
            raise ValueError("Google Elevation API key must not be empty.")

        if batch_size <= 0:
            raise ValueError("batch_size must be greater than zero.")

        self._api_key = api_key
        self._timeout = timeout
        self._batch_size = batch_size

    def get_elevations(
        self,
        points: list[Point],
    ) -> list[GoogleElevationPoint]:
        """
        Retrieve Google terrain elevation for all supplied points.
        """

        if not points:
            return []

        result: list[GoogleElevationPoint] = []

        for start in range(
            0,
            len(points),
            self._batch_size,
        ):
            batch = points[start : start + self._batch_size]

            result.extend(self._get_batch(batch))

        return result

    def _get_batch(
        self,
        points: list[Point],
    ) -> list[GoogleElevationPoint]:
        locations = "|".join(f"{point.latitude},{point.longitude}" for point in points)

        response = requests.get(
            self.BASE_URL,
            params={
                "locations": locations,
                "key": self._api_key,
            },
            timeout=self._timeout,
        )

        response.raise_for_status()

        payload = response.json()

        status = payload.get("status")

        if status != "OK":
            raise RuntimeError(
                "Google Elevation API failed: "
                f"{status}: "
                f"{payload.get('error_message', '')}"
            )

        results = payload.get("results", [])

        if len(results) != len(points):
            raise RuntimeError(
                "Google Elevation API returned unexpected "
                f"number of results: expected {len(points)}, "
                f"got {len(results)}"
            )

        return [
            GoogleElevationPoint(
                latitude=result["location"]["lat"],
                longitude=result["location"]["lng"],
                elevation=result["elevation"],
                resolution=result.get("resolution"),
            )
            for result in results
        ]
