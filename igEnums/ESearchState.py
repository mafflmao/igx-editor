# ESearchState.py

from enum import Enum

class ESearchState(Enum):
    eSS_None = "eSS_None"
    eSS_GroundCheck = "eSS_GroundCheck"
    eSS_BlockerCheck = "eSS_BlockerCheck"
