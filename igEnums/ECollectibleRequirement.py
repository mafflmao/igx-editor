# ECollectibleRequirement.py

from enum import Enum

class ECollectibleRequirement(Enum):
    eCR_None = "eCR_None"
    eCR_IsDriver = "eCR_IsDriver"
    eCR_IsTrap = "eCR_IsTrap"
    eCR_TreasurePlaced = "eCR_TreasurePlaced"
    eCR_VehicleLand = "eCR_VehicleLand"
    eCR_VehicleAir = "eCR_VehicleAir"
    eCR_VehicleWater = "eCR_VehicleWater"
