# EScaleBeamState.py

from enum import Enum

class EScaleBeamState(Enum):
    eSBS_Invalid = "eSBS_Invalid"
    eSBS_Idle = "eSBS_Idle"
    eSBS_Charging = "eSBS_Charging"
    eSBS_Active = "eSBS_Active"
    eSBS_Cooldown = "eSBS_Cooldown"
