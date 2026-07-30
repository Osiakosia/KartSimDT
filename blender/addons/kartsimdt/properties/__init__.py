from . import calibration


def register() -> None:
    calibration.register()


def unregister() -> None:
    calibration.unregister()
