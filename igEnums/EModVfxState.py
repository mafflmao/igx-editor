# EModVfxState.py

from enum import Enum

class EModVfxState(Enum):
    eMVS_Idle = "eMVS_Idle"
    eMVS_Driving = "eMVS_Driving"
    eMVS_Jumping = "eMVS_Jumping"
    eMVS_FakeFullThrottle = "eMVS_FakeFullThrottle"
