# EMagicMomentReason.py

from enum import Enum

class EMagicMomentReason(Enum):
    eMMR_ToyRemoved = "eMMR_ToyRemoved"
    eMMR_TooManyCharacterToys = "eMMR_TooManyCharacterToys"
    eMMR_InvalidToy = "eMMR_InvalidToy"
    eMMR_ErrorOnToy = "eMMR_ErrorOnToy"
    eMMR_PlayerDeath = "eMMR_PlayerDeath"
    eMMR_ManualRequest = "eMMR_ManualRequest"
    eMMR_MapStart = "eMMR_MapStart"
    eMMR_PortalVersion = "eMMR_PortalVersion"
    eMMR_PortalCount = "eMMR_PortalCount"
    eMMR_ResetToy = "eMMR_ResetToy"
    eMMR_ResetVehicle = "eMMR_ResetVehicle"
    eMMR_TooManyVehicleToys = "eMMR_TooManyVehicleToys"
    eMMR_VehicleAdded = "eMMR_VehicleAdded"
    eMMR_VehicleRequired = "eMMR_VehicleRequired"
    eMMR_TooManyTrapToys = "eMMR_TooManyTrapToys"
    eMMR_OnlineError = "eMMR_OnlineError"
