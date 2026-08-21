"""
google_elevation_kml_writer.py

Writes Google terrain elevation into a Track Survey KML.

The original KML is never modified.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from .google_elevation_client import GoogleElevationPoint


class GoogleElevationKmlWriter:
    """
    Writes Google elevation values into KML coordinates.
    """

    KML_NAMESPACE = "http://www.opengis.net/kml/2.2"

    def write(
        self,
        source_file: Path,
        elevations: list[GoogleElevationPoint],
        output_file: Path,
    ) -> None:
        """
        Create a new KML containing Google elevation values.

        The order of elevation points must match the
        order of KML coordinates.
        """

        if not source_file.exists():
            raise FileNotFoundError(f"Source KML file not found: {source_file}")

        if not elevations:
            raise ValueError("Google elevation dataset is empty.")

        tree = ET.parse(source_file)
        root = tree.getroot()

        namespace = {
            "kml": self.KML_NAMESPACE,
        }

        document = root.find(
            "kml:Document",
            namespace,
        )

        if document is None:
            raise ValueError("KML Document element is missing.")

        placemark = document.find(
            "kml:Placemark",
            namespace,
        )

        if placemark is None:
            raise ValueError("KML Placemark element is missing.")

        line = placemark.find(
            "kml:LineString",
            namespace,
        )

        if line is None:
            raise ValueError("KML LineString element is missing.")

        coordinates_element = line.find(
            "kml:coordinates",
            namespace,
        )

        if coordinates_element is None:
            raise ValueError("KML coordinates element is missing.")

        rows = coordinates_element.text or ""
        coordinate_rows = rows.strip().split()

        if len(coordinate_rows) != len(elevations):
            raise ValueError(
                "KML coordinate count and Google elevation "
                "count do not match. "
                f"KML={len(coordinate_rows)}, "
                f"Google={len(elevations)}."
            )

        new_coordinates: list[str] = []

        for row, google_point in zip(
            coordinate_rows,
            elevations,
            strict=True,
        ):
            values = row.split(",")

            if len(values) < 2:
                raise ValueError(f"Invalid KML coordinate: {row}")

            longitude = values[0]
            latitude = values[1]

            new_coordinates.append(
                f"{longitude},{latitude},{google_point.elevation:.6f}"
            )

        coordinates_element.text = "\n" + "\n".join(new_coordinates) + "\n"

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        ET.register_namespace(
            "",
            self.KML_NAMESPACE,
        )

        tree.write(
            output_file,
            encoding="utf-8",
            xml_declaration=True,
        )
