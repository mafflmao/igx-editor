# EDriverState.py

from enum import Enum

class EDriverState(Enum):
    eDS_Transitioning = "eDS_Transitioning"
    eDS_Driving = "eDS_Driving"
    eDS_Disembarking = "eDS_Disembarking"
    eDS_OnFoot = "eDS_OnFoot"
