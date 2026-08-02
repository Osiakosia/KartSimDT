"""
Calibration service.

Load and save scene calibration.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

import bpy


def get_transform_path() -> Path:
    """
    Return scene_transform.json belonging to the current .blend scene.
    """

    blend_file = Path(bpy.data.filepath)

    if not blend_file:
        raise RuntimeError("Current Blender scene has not been saved.")

    path = blend_file.parent / "scene_transform.json"

    print("BLEND FILE =", blend_file)
    print("TRANSFORM PATH =", path)

    return path


def _default_orthophoto() -> dict[str, Any]:
    return {
        "scale": 1.0,
        "rotation": 0.0,
        "offset_x": 0.0,
        "offset_y": 0.0,
    }


def _default_track_centerline() -> dict[str, Any]:
    return {
        "scale": 1.0,
        "rotation_deg": 0.0,
        "offset_x": 0.0,
        "offset_y": 0.0,
        "offset_z": 0.0,
    }


def load_calibration() -> dict[str, Any]:
    """
    Load calibration from JSON.

    Missing sections are created automatically.
    """

    path = get_transform_path()

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = cast(dict[str, Any], json.load(file))

    changed = False

    if "version" not in data:
        data["version"] = 1
        changed = True

    if "orthophoto" not in data:
        data["orthophoto"] = _default_orthophoto()
        changed = True

    if "track_centerline" not in data:
        data["track_centerline"] = _default_track_centerline()
        changed = True

    if changed:
        save_calibration(data)

    return data


def save_calibration(
    data: dict[str, Any],
) -> None:
    """
    Save calibration to JSON.
    """

    path = get_transform_path()

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=4,
        )


def _get_section(
    name: str,
) -> dict[str, Any]:
    """
    Return calibration section.
    """

    data = load_calibration()

    return cast(dict[str, Any], data[name])


def _set_section(
    name: str,
    value: dict[str, Any],
) -> None:
    """
    Save calibration section.
    """

    data = load_calibration()

    data[name] = value

    save_calibration(data)


def default_calibration() -> dict[str, Any]:
    """
    Return complete default calibration.
    """

    return {
        "version": 1,
        "orthophoto": _default_orthophoto(),
        "track_centerline": _default_track_centerline(),
    }


def reset_calibration() -> dict[str, Any]:
    """
    Reset only Orthophoto calibration.

    Preserve all other calibration sections.
    """

    data = load_calibration()

    data["orthophoto"] = _default_orthophoto()

    save_calibration(data)

    return data


def get_orthophoto_transform() -> dict[str, Any]:
    """
    Return orthophoto transform.
    """

    return _get_section("orthophoto")


def set_orthophoto_transform(
    transform: dict[str, Any],
) -> None:
    """
    Save orthophoto transform.
    """

    _set_section(
        "orthophoto",
        transform,
    )
