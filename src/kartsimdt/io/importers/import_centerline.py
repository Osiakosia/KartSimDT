"""
Import Centerline JSON into Blender.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast


def load_centerline(path: Path) -> dict[str, Any]:
    """
    Load Centerline JSON.
    """

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return cast(dict[str, Any], json.load(file))


def main() -> None:

    root = Path(__file__).resolve().parents[2]

    json_file = root / "data" / "exports" / "centerline.json"

    data = load_centerline(json_file)

    print("=" * 60)
    print("KartSimDT Blender Import")
    print("=" * 60)
    print()

    print(f"Geometry : {data['geometry']}")
    print(f"Name     : {data['name']}")
    print(f"Points   : {data['point_count']}")
    print()

    print("Import Preview : PASS")


if __name__ == "__main__":
    main()
