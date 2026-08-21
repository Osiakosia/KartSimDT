"""
Track design domain model.

Defines track-specific design parameters independently
from Blender or any other visualization platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import yaml

if TYPE_CHECKING:
    from kartsimdt.track.context import TrackContext


@dataclass(frozen=True, slots=True)
class WidthZone:
    """Variable-width road zone."""

    name: str
    start_index: int
    end_index: int
    width_m: float


@dataclass(frozen=True, slots=True)
class StartFinish:
    """Start/finish definition."""

    centerline_index: int
    straight_start_index: int
    straight_end_index: int
    straight_length_m: float


@dataclass(frozen=True, slots=True)
class RoadDesign:
    """Road design parameters."""

    default_width_m: float
    width_zones: list[WidthZone] = field(
        default_factory=list,
    )


@dataclass(frozen=True, slots=True)
class TrackDesign:
    """Track-specific design definition."""

    road: RoadDesign
    start_finish: StartFinish
    kerbs: list[Any] = field(default_factory=list)
    terrain: dict[str, Any] = field(default_factory=dict)
    runoff: list[Any] = field(default_factory=list)
    objects: list[Any] = field(default_factory=list)

    @classmethod
    def from_yaml(
        cls,
        path: str | Path,
    ) -> TrackDesign:
        """Load track design from YAML."""

        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(f"Track design file not found: {path}")

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            raw_data = yaml.safe_load(file) or {}

        data = cast(dict[str, Any], raw_data)

        road_data = cast(
            dict[str, Any],
            data["road"],
        )

        start_finish_data = cast(
            dict[str, Any],
            data["start_finish"],
        )

        width_zones = [
            WidthZone(
                name=zone["name"],
                start_index=zone["start_index"],
                end_index=zone["end_index"],
                width_m=zone["width_m"],
            )
            for zone in cast(
                list[dict[str, Any]],
                road_data.get("width_zones", []),
            )
        ]

        return cls(
            road=RoadDesign(
                default_width_m=road_data["default_width_m"],
                width_zones=width_zones,
            ),
            start_finish=StartFinish(
                centerline_index=start_finish_data["centerline_index"],
                straight_start_index=start_finish_data["straight_start_index"],
                straight_end_index=start_finish_data["straight_end_index"],
                straight_length_m=start_finish_data["straight_length_m"],
            ),
            kerbs=data.get("kerbs", []),
            terrain=data.get("terrain", {}),
            runoff=data.get("runoff", []),
            objects=data.get("objects", []),
        )

    @classmethod
    def from_context(
        cls,
        context: TrackContext,
    ) -> TrackDesign:
        """Load design using a resolved track context."""

        return cls.from_yaml(
            context.track_design_yaml,
        )
