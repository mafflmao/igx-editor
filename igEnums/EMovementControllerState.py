# EMovementControllerState.py

from enum import Enum

class EMovementControllerState(Enum):
    eMCS_Invalid = "eMCS_Invalid"
    eMCS_Active = "eMCS_Active"
    eMCS_Paused = "eMCS_Paused"
    eMCS_Completed = "eMCS_Completed"
    eMCS_Inactive = "eMCS_Inactive"
