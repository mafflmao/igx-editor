# EMagicMomentErrorType.py

from enum import Enum

class EMagicMomentErrorType(Enum):
    eMMET_None = "eMMET_None"
    eMMET_TooManyCharacterToys = "eMMET_TooManyCharacterToys"
    eMMET_TooManyCharacterToysForPlayer = "eMMET_TooManyCharacterToysForPlayer"
    eMMET_InvalidToy = "eMMET_InvalidToy"
    eMMET_ErrorOnToy = "eMMET_ErrorOnToy"
    eMMET_PortalDisconnected = "eMMET_PortalDisconnected"
    eMMET_PortalVersion = "eMMET_PortalVersion"
    eMMET_PortalCount = "eMMET_PortalCount"
    eMMET_RegisteredCharacterRemoved = "eMMET_RegisteredCharacterRemoved"
    eMMET_TooManyVehicleToys = "eMMET_TooManyVehicleToys"
    eMMET_VehicleWrongElement = "eMMET_VehicleWrongElement"
    eMMET_VehicleWrongType = "eMMET_VehicleWrongType"
    eMMET_TooManyTrapToys = "eMMET_TooManyTrapToys"
    eMMET_RemoteOnlineError = "eMMET_RemoteOnlineError"
    eMMET_ToyNotInstalled = "eMMET_ToyNotInstalled"
