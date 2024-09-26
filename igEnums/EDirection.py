# EDirection.py

from enum import Enum

class EDirection(Enum):
    eD_Forwards = "eD_Forwards"
    eD_Backwards = "eD_Backwards"
    eD_Leftwards = "eD_Leftwards"
    eD_Rightwards = "eD_Rightwards"
    eD_LastPressedStickDirection = "eD_LastPressedStickDirection"
