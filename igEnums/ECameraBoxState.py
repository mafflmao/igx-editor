# ECameraBoxState.py

from enum import Enum

class ECameraBoxState(Enum):
    eCBS_Invalid = "eCBS_Invalid"
    eCBS_Reset = "eCBS_Reset"
    eCBS_ProgressedThrough = "eCBS_ProgressedThrough"
    eCBS_Progressing = "eCBS_Progressing"
    eCBS_BacktrackedThrough = "eCBS_BacktrackedThrough"
