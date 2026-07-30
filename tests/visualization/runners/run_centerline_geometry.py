"""
Run CenterlineGeometry tests.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/visualization/test_centerline_geometry.py",
            "-v",
        ],
        cwd=ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
