# ERaceAIState.py

from enum import Enum

class ERaceAIState(Enum):
    eRAIS_MovementLocked = "eRAIS_MovementLocked"
    eRAIS_RubberBurning = "eRAIS_RubberBurning"
    eRAIS_Enabled = "eRAIS_Enabled"
    eRAIS_ChooseObjective = "eRAIS_ChooseObjective"
    eRAIS_Overtake = "eRAIS_Overtake"
    eRAIS_Dead = "eRAIS_Dead"
