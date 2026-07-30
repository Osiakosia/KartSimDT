import bpy

from blender.operators import (
    BuildEngineeringSceneOperator,
    ExportCalibrationOperator,
)
from blender.panels import (
    KartSimDTPanel,
)

CLASSES = (
    BuildEngineeringSceneOperator,
    ExportCalibrationOperator,
    KartSimDTPanel,
)


def register() -> None:
    print("REGISTER CALLED")

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister() -> None:
    print("UNREGISTER CALLED")

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
