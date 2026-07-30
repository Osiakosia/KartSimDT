from . import (
    build_engineering_scene,
    export_calibration,
    reset_calibration,
    save_calibration,
)


def register() -> None:
    build_engineering_scene.register()
    export_calibration.register()
    save_calibration.register()
    reset_calibration.register()


def unregister() -> None:
    reset_calibration.unregister()
    save_calibration.unregister()
    export_calibration.unregister()
    build_engineering_scene.unregister()
