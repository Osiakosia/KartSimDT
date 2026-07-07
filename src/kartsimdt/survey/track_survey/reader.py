"""
reader.py

KartSimDT Track Survey Module

Reads Google Earth KML survey files.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from .exceptions import InvalidTrackSurveyError
from .raw import TrackSurveyRawData


class KmlReader:
    """
    Reads Google Earth KML survey files.
    """

    KML_NAMESPACE = {
        "kml": "http://www.opengis.net/kml/2.2",
    }

    def _read_document(
        self,
        root: ET.Element,
    ) -> ET.Element:
        """
        Read the KML Document element.
        """

        document = root.find(
            "kml:Document",
            self.KML_NAMESPACE,
        )

        if document is None:
            raise InvalidTrackSurveyError("KML Document element is missing.")

        return document

    def _read_metadata(
        self,
        document: ET.Element,
    ) -> dict[str, str]:
        """
        Read KML document metadata.
        """

        metadata: dict[str, str] = {}

        metadata["name"] = document.findtext(
            "kml:name",
            default="",
            namespaces=self.KML_NAMESPACE,
        )

        metadata["description"] = document.findtext(
            "kml:description",
            default="",
            namespaces=self.KML_NAMESPACE,
        )

        return metadata

    def _read_coordinates(
        self,
        document: ET.Element,
    ) -> list[tuple[float, float, float | None]]:
        """
        Read LineString coordinates.
        """

        placemark = document.find(
            "kml:Placemark",
            self.KML_NAMESPACE,
        )

        if placemark is None:
            raise InvalidTrackSurveyError("Placemark element is missing.")

        line = placemark.find(
            "kml:LineString",
            self.KML_NAMESPACE,
        )

        if line is None:
            raise InvalidTrackSurveyError("LineString element is missing.")

        coordinate_text = line.findtext(
            "kml:coordinates",
            default="",
            namespaces=self.KML_NAMESPACE,
        )

        coordinates: list[
            tuple[
                float,
                float,
                float | None,
            ]
        ] = []

        for row in coordinate_text.strip().split():

            values = row.split(",")

            longitude = float(values[0])
            latitude = float(values[1])

            elevation = None

            if len(values) >= 3:
                value = float(values[2])
                elevation = value if value != 0.0 else None
            else:
                elevation = None

            coordinates.append(
                (
                    longitude,
                    latitude,
                    elevation,
                )
            )

        return coordinates

    def read(
        self,
        file_path: Path,
    ) -> TrackSurveyRawData:
        """
        Read a Google Earth KML survey file.
        """

        try:
            tree = ET.parse(file_path)

        except ET.ParseError as error:
            raise InvalidTrackSurveyError(f"Invalid KML file: {file_path}") from error

        root = tree.getroot()

        document = self._read_document(root)

        metadata = self._read_metadata(document)

        coordinates = self._read_coordinates(document)

        return TrackSurveyRawData(
            metadata=metadata,
            coordinates=coordinates,
        )
