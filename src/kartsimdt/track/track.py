from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class Track:
    """Track data container loaded from a track directory."""

    def __init__(self, track_dir: str | Path) -> None:
        self.root = Path(track_dir)

        if not self.root.is_dir():
            raise FileNotFoundError(f"Track directory does not exist: {self.root}")

        self.name = self.root.name

    @property
    def metadata_path(self) -> Path:
        return self.root / "metadata.yaml"

    @property
    def design_path(self) -> Path:
        return self.root / "design" / "track_design.yaml"

    def load_metadata(self) -> dict[str, Any]:
        return self._load_yaml(self.metadata_path)

    def load_design(self) -> dict[str, Any]:
        return self._load_yaml(self.design_path)

    @staticmethod
    def _load_yaml(path: Path) -> dict[str, Any]:
        if not path.is_file():
            raise FileNotFoundError(f"YAML file does not exist: {path}")

        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if not isinstance(data, dict):
            raise ValueError(f"Expected mapping in YAML file: {path}")

        return data
