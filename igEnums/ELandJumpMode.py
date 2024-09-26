# ELandJumpMode.py

from enum import Enum

class ELandJumpMode(Enum):
    eLJM_None = "eLJM_None"
    eLJM_NoJump = "eLJM_NoJump"
    eLJM_WorldUp = "eLJM_WorldUp"
    eLJM_EntityUp = "eLJM_EntityUp"
    eLJM_FlattenedEntityUp = "eLJM_FlattenedEntityUp"
    eLJM_Count = "eLJM_Count"
