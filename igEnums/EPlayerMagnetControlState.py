# EPlayerMagnetControlState.py

from enum import Enum

class EPlayerMagnetControlState(Enum):
    ePMCS_Disabled = "ePMCS_Disabled"
    ePMCS_PullOnly = "ePMCS_PullOnly"
    ePMCS_PushOnly = "ePMCS_PushOnly"
    ePMCS_PushAndPull = "ePMCS_PushAndPull"
