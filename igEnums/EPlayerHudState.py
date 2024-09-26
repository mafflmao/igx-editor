# EPlayerHudState.py

from enum import Enum

class EPlayerHudState(Enum):
    ePHS_None = "ePHS_None"
    ePHS_OnFoot = "ePHS_OnFoot"
    ePHS_OnFootNearTransition = "ePHS_OnFootNearTransition"
    ePHS_OnFootFlipped = "ePHS_OnFootFlipped"
    ePHS_InVehicleDriver = "ePHS_InVehicleDriver"
    ePHS_InVehiclePassenger = "ePHS_InVehiclePassenger"
