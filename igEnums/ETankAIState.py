# ETankAIState.py

from enum import Enum

class ETankAIState(Enum):
    eTAIS_Approaching = "eTAIS_Approaching"
    eTAIS_BackOff = "eTAIS_BackOff"
    eTAIS_Wander = "eTAIS_Wander"
