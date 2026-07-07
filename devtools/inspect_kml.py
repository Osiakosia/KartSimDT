"""
inspect_kml.py

KartSimDT Engineering Inspector

Inspects a Google Earth KML centerline file.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

# ============================================================================
# Project Paths
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATASET = PROJECT_ROOT / "tests" / "data" / "aukstadvaris" / "survey" / "centerline.kml"

KML_NS = {"kml": "http://www.opengis.net/kml/2.2"}


# ============================================================================
# Helpers
# ============================================================================


def separator(title: str) -> None:
    """Print section separator."""
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


# ============================================================================
# Main
# ============================================================================


def main() -> None:

    separator("KartSimDT KML Inspector")

    print("Source")
    print("-" * 60)
    print(f"File : {DATASET.name}")
    print(f"Path : {DATASET}")

    tree = ET.parse(DATASET)
    root = tree.getroot()

    # ---------------------------------------------------------------------
    # XML
    # ---------------------------------------------------------------------

    separator("XML Information")

    print(f"Root Element : {root.tag}")

    # ---------------------------------------------------------------------
    # Document
    # ---------------------------------------------------------------------

    document = root.find("kml:Document", KML_NS)

    separator("Document")

    if document is None:
        print("Document not found")
        return

    name = document.findtext("kml:name", default="", namespaces=KML_NS)
    description = document.findtext(
        "kml:description",
        default="",
        namespaces=KML_NS,
    )

    print(f"Name        : {name}")
    print(f"Description : {description}")

    # ---------------------------------------------------------------------
    # Placemark
    # ---------------------------------------------------------------------

    placemarks = document.findall("kml:Placemark", KML_NS)

    separator("Placemark")

    print(f"Count : {len(placemarks)}")

    for i, placemark in enumerate(placemarks, start=1):

        pname = placemark.findtext(
            "kml:name",
            default="",
            namespaces=KML_NS,
        )

        print(f"\nPlacemark {i}")
        print(f"Name : {pname}")

        line = placemark.find("kml:LineString", KML_NS)

        if line is not None:
            print("Geometry : LineString")

            tessellate = line.findtext(
                "kml:tessellate",
                default="",
                namespaces=KML_NS,
            )

            altitude = line.findtext(
                "kml:altitudeMode",
                default="",
                namespaces=KML_NS,
            )

            extrude = line.findtext(
                "kml:extrude",
                default="",
                namespaces=KML_NS,
            )

            print(f"Tessellate  : {tessellate}")
            print(f"Extrude     : {extrude}")
            print(f"Altitude    : {altitude}")

            coordinates = line.findtext(
                "kml:coordinates",
                default="",
                namespaces=KML_NS,
            )

            points = []

            for row in coordinates.strip().split():

                lon, lat, *rest = row.split(",")

                elev = float(rest[0]) if rest else 0.0

                points.append(
                    (
                        float(lon),
                        float(lat),
                        elev,
                    )
                )

            separator("Coordinates")

            print(f"Point Count : {len(points)}")

            if points:

                first = points[0]
                last = points[-1]

                print("\nFirst Point")
                print(f"Longitude : {first[0]:.8f}")
                print(f"Latitude  : {first[1]:.8f}")
                print(f"Elevation : {first[2]:.3f}")

                print("\nLast Point")
                print(f"Longitude : {last[0]:.8f}")
                print(f"Latitude  : {last[1]:.8f}")
                print(f"Elevation : {last[2]:.3f}")

                north = max(p[1] for p in points)
                south = min(p[1] for p in points)
                east = max(p[0] for p in points)
                west = min(p[0] for p in points)

                separator("Bounding Box")

                print(f"North : {north:.8f}")
                print(f"South : {south:.8f}")
                print(f"East  : {east:.8f}")
                print(f"West  : {west:.8f}")

                separator("Statistics")

                print(f"Total Points      : {len(points)}")
                print(f"Elevation Present : " f"{any(p[2] != 0.0 for p in points)}")
                print(f"Closed Track      : " f"{points[0] == points[-1]}")

    separator("Inspection Complete")


if __name__ == "__main__":
    main()
