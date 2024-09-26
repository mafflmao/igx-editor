# EFlyingLinearAIState.py

from enum import Enum

class EFlyingLinearAIState(Enum):
    eFLAIS_WaitingForAttach = "eFLAIS_WaitingForAttach"
    eFLAIS_Transitioning = "eFLAIS_Transitioning"
    eFLAIS_Flying = "eFLAIS_Flying"
    eFLAIS_Attacking = "eFLAIS_Attacking"
