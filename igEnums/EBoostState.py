# EBoostState.py

from enum import Enum

class EBoostState(Enum):
    eBS_None = "eBS_None"
    eBS_TransitionIn = "eBS_TransitionIn"
    eBS_Active = "eBS_Active"
    eBS_DelayOut = "eBS_DelayOut"
    eBS_TransitionOut = "eBS_TransitionOut"
