# ESplineMoveMode.py

from enum import Enum

class ESplineMoveMode(Enum):
    eSMM_PauseAtEnd = "eSMM_PauseAtEnd"
    eSMM_PingPong = "eSMM_PingPong"
    eSMM_Loop = "eSMM_Loop"
    eSMM_DetachAtEnd = "eSMM_DetachAtEnd"
    eSMM_TrackRatio = "eSMM_TrackRatio"
