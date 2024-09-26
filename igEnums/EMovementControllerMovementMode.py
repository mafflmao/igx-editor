# EMovementControllerMovementMode.py

from enum import Enum

class EMovementControllerMovementMode(Enum):
    eMCMM_SetPosition = "eMCMM_SetPosition"
    eMCMM_SetVelocities = "eMCMM_SetVelocities"
    eMCMM_AddMoveVector = "eMCMM_AddMoveVector"
