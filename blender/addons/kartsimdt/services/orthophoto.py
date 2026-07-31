"""
KartSimDT Orthophoto Service

Responsibilities
----------------
- Find the Orthophoto object.
- Provide access to the object for calibration services.

Does NOT
---------
- Draw UI.
- Save calibration.
- Modify Blender properties.
"""

from __future__ import annotations

import bpy

ORTHOPHOTO_OBJECT_NAME = "Orthophoto"


def get_orthophoto() -> bpy.types.Object | None:
    """
    Return the Orthophoto object.

    Returns
    -------
    bpy.types.Object | None
        Orthophoto object if found, otherwise None.
    """

    return bpy.data.objects.get(ORTHOPHOTO_OBJECT_NAME)


def apply_scale(scale: float) -> bool:
    """
    Apply uniform scale to the Orthophoto object.

    Parameters
    ----------
    scale
        Uniform scale factor.

    Returns
    -------
    bool
        True if the object was found and updated,
        otherwise False.
    """

    obj = get_orthophoto()

    if obj is None:
        return False

    obj.scale.x = scale
    obj.scale.y = scale
    obj.scale.z = scale

    return True


def apply_rotation(angle: float) -> bool:
    """
    Apply Z-axis rotation to the Orthophoto object.
    """

    obj = get_orthophoto()

    if obj is None:
        return False

    obj.rotation_euler.z = angle

    return True


def apply_offset_x(offset: float) -> bool:
    """
    Apply X offset to the Orthophoto object.
    """

    obj = get_orthophoto()

    if obj is None:
        return False

    obj.location.x = offset

    return True


def apply_offset_y(offset: float) -> bool:
    """
    Apply Y offset to the Orthophoto object.
    """

    obj = get_orthophoto()

    if obj is None:
        return False

    obj.location.y = offset

    return True
