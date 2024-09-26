# EVirtualControllerMode.py

from enum import Enum

class EVirtualControllerMode(Enum):
    eVCM_Default = "eVCM_Default"
    eVCM_CoopSwap = "eVCM_CoopSwap"
    eVCM_ShrinkRay = "eVCM_ShrinkRay"
    eVCM_Magnet = "eVCM_Magnet"
    eVCM_Interact = "eVCM_Interact"
    eVCM_Teleport = "eVCM_Teleport"
    eVCM_VehicleMods = "eVCM_VehicleMods"
    eVCM_LegendaryTreasurePlace = "eVCM_LegendaryTreasurePlace"
    eVCM_LegendaryTreasurePickup = "eVCM_LegendaryTreasurePickup"
    eVCM_LockPick = "eVCM_LockPick"
    eVCM_All = "eVCM_All"
    eVCM_Max = "eVCM_Max"
