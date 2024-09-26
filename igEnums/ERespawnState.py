# ERespawnState.py

from enum import Enum

class ERespawnState(Enum):
    eRS_Delay = "eRS_Delay"
    eRS_WaitForSafe = "eRS_WaitForSafe"
    eRS_Searching = "eRS_Searching"
    eRS_TransitionIn = "eRS_TransitionIn"
    eRS_TransitionOut = "eRS_TransitionOut"
    eRS_WaitToFinish = "eRS_WaitToFinish"
