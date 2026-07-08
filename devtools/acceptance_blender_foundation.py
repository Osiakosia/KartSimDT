"""
acceptance_blender_foundation.py

Visualization Foundation acceptance pipeline.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def separator(title: str) -> None:
    """Print section separator."""

    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


def run(script: str) -> None:
    """Run a devtool script."""

    separator(script)

    subprocess.run(
        [
            sys.executable,
            PROJECT_ROOT / "devtools" / script,
        ],
        check=True,
    )


def main() -> None:

    separator("KartSimDT Visualization Foundation")

    run("inspect_blender_curve.py")

    run("report_blender_curve.py")

    separator("Acceptance Complete")


if __name__ == "__main__":
    main()
