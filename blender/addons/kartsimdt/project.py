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
    Add KartSimDT project root and Core package to Python paths.
    """

    prefs = bpy.context.preferences.addons[__package__].preferences

    print("prefs.project_root =", repr(prefs.project_root))

    project_root = Path(prefs.project_root)

    print("project_root =", repr(project_root))

    if not project_root:
        raise RuntimeError("Project Root is not configured.")

    if not project_root.exists():
        raise RuntimeError(f"Project Root does not exist:\n{project_root}")

    blender_dir = project_root / "blender"

    print("blender_dir =", repr(blender_dir))

    if not blender_dir.exists():
        raise RuntimeError(f"'blender' directory not found:\n{blender_dir}")

    project_src = project_root / "src"

    if not project_src.exists():
        raise RuntimeError(f"'src' directory not found:\n{project_src}")

    project_src_str = str(project_src)

    if project_src_str not in sys.path:
        sys.path.insert(
            0,
            project_src_str,
        )

    # Blender addon already owns the "kartsimdt" package.
    # Extend its package path so Core submodules can be found.
    import kartsimdt

    core_package = project_src / "kartsimdt"
    core_package_str = str(core_package)

    if core_package_str not in kartsimdt.__path__:
        kartsimdt.__path__.append(
            core_package_str,
        )

    print("=" * 60)
    print("KartSimDT")
    print(f"Project Root : {project_root}")
    print(f"Blender Dir  : {blender_dir}")
    print(f"Project Src  : {project_src}")
    print("Core Package :", core_package)
    print("=" * 60)

    return project_root


def get_track_context():
    """
    Return the currently configured track context.
    """

    from kartsimdt.track.resolver import TrackResolver

    prefs = bpy.context.preferences.addons[__package__].preferences

    project_root = get_project_root()

    tracks_root = project_root / "data" / "tracks"

    resolver = TrackResolver(
        tracks_root=tracks_root,
    )

    return resolver.resolve(
        prefs.track_name,
    )
