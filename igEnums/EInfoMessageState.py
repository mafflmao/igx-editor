# EInfoMessageState.py

from enum import Enum

class EInfoMessageState(Enum):
    eIMS_None = "eIMS_None"
    eIMS_Loading = "eIMS_Loading"
    eIMS_SkipAttempt = "eIMS_SkipAttempt"
    eIMS_SkipWait = "eIMS_SkipWait"
    eIMS_Paused = "eIMS_Paused"
