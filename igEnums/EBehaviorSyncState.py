# EBehaviorSyncState.py

from enum import Enum

class EBehaviorSyncState(Enum):
    eBSS_Inactive = "eBSS_Inactive"
    eBSS_Transitioning = "eBSS_Transitioning"
    eBSS_EnteredState = "eBSS_EnteredState"
    eBSS_InState = "eBSS_InState"
    eBSS_LeftState = "eBSS_LeftState"
