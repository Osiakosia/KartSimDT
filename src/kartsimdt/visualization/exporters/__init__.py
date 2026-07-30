"""
centerline_json_exporter.py

Export CenterlineGeometry to JSON.
"""

from __future__ import annotations

from pathlib import Path

from kartsimdt.visualization.geometry.centerline import (
    CenterlineGeometry,
)


class CenterlineJsonExporter:
    """
    Exports CenterlineGeometry to JSON.
    """

    def export(
        self,
        geometry: CenterlineGeometry,
        output_file: Path,
    ) -> None:
        """
        Export geometry to JSON.
        """

        raise NotImplementedError
