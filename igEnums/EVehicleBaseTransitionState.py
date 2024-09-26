# EVehicleBaseTransitionState.py

from enum import Enum

class EVehicleBaseTransitionState(Enum):
    eVBTS_Disabled = "eVBTS_Disabled"
    eVBTS_Eligible = "eVBTS_Eligible"
    eVBTS_Transitioning = "eVBTS_Transitioning"
    eVBTS_TransitionComplete = "eVBTS_TransitionComplete"
