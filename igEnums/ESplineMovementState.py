# ESplineMovementState.py

from enum import Enum

class ESplineMovementState(Enum):
    eSMS_None = "eSMS_None"
    eSMS_Playing = "eSMS_Playing"
    eSMS_PlayingReversed = "eSMS_PlayingReversed"
    eSMS_Paused = "eSMS_Paused"
    eSMS_Stopped = "eSMS_Stopped"
