from __future__ import annotations

import sys
from pathlib import Path

import bpy


def get_project_root() -> Path:
    """
    Return configured project root.
    """

    print("__package__ =", __package__)
    print("addons =", list(bpy.context.preferences.addons.keys()))

    addon = bpy.context.preferences.addons.get(__package__)

    print("addon =", addon)

    if addon is None:
        raise RuntimeError(f"Addon '{__package__}' not found.")

    print("preferences =", addon.preferences)

    if addon.preferences is None:
        raise RuntimeError("Addon preferences are None.")

    prefs = addon.preferences

    print("project_root =", prefs.project_root)

    project_root = Path(prefs.project_root)

    if not project_root.exists():
        raise RuntimeError(f"Project Root does not exist:\n{project_root}")

    return project_root


def setup_project_path() -> Path:
    """
    Add KartSimDT project root to sys.path.
    """

    prefs = bpy.context.preferences.addons[__package__].preferences

    print("prefs.project_root =", repr(prefs.project_root))

    project_root = Path(prefs.project_root)

    print("project_root =", repr(project_root))

    project_root = Path(prefs.project_root)

    if not project_root:
        raise RuntimeError("Project Root is not configured.")

    if not project_root.exists():
        raise RuntimeError(f"Project Root does not exist:\n{project_root}")
    print("blender_dir =", repr(project_root / "blender"))

    blender_dir = project_root / "blender"

    if not blender_dir.exists():
        raise RuntimeError(f"'blender' directory not found:\n{blender_dir}")

    project_root_str = str(project_root)

    if project_root_str not in sys.path:
        sys.path.insert(
            0,
            project_root_str,
        )

    print("=" * 60)
    print("KartSimDT")
    print(f"Project Root : {project_root}")
    print(f"Blender Dir  : {blender_dir}")
    print("=" * 60)

    return project_root
