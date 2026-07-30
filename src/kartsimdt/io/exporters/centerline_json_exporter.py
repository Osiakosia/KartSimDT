"""
centerline_json_exporter.py

Export CenterlineGeometry to JSON.
"""

from __future__ import annotations

import json
from pathlib import Path

from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)


class CenterlineJsonExporter:
    """
    Exports CenterlineGeometry to JSON.
    """

    def build_json(
        self,
        geometry: CenterlineGeometry,
    ) -> dict:
        """
        Build JSON representation of the centerline geometry.
        """

        return {
            "format": "KartSimDT",
            "version": 1,
            "geometry": "Centerline",
            "coordinate_system": "Local",
            "name": geometry.name,
            "point_count": len(geometry.points),
            "points": [
                {
                    "x": point.x,
                    "y": point.y,
                    "z": point.z,
                }
                for point in geometry.points
            ],
        }

    def export(
        self,
        geometry: CenterlineGeometry,
        output_file: Path,
    ) -> None:
        """
        Export geometry to JSON.
        """

        data = self.build_json(geometry)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

        print("=" * 60)
        print("KartSimDT Centerline JSON Export")
        print("=" * 60)
        print()

        print(f"Geometry : {geometry.name}")
        print(f"Points   : {len(geometry.points)}")
        print(f"Output   : {output_file}")

        print()
        print("Status : PASS")
