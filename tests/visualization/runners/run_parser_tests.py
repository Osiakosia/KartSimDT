"""
Run Visualization validator tests.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/visualization/test_visualization_parser.py",
            "-v",
        ],
        cwd=PROJECT_ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
