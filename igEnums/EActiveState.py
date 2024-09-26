# EActiveState.py

from enum import Enum

class EActiveState(Enum):
    eAS_WaitingToMove = "eAS_WaitingToMove"
    eAS_MovingToDestination = "eAS_MovingToDestination"
    eAS_ReachedFinalDestination = "eAS_ReachedFinalDestination"
