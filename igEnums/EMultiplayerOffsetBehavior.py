# EMultiplayerOffsetBehavior.py

from enum import Enum

class EMultiplayerOffsetBehavior(Enum):
    eMOB_NoOffset = "eMOB_NoOffset"
    eMOB_OnlyStartingOffset = "eMOB_OnlyStartingOffset"
    eMOB_OnlyLandingOffset = "eMOB_OnlyLandingOffset"
    eMOB_AlwaysOffset = "eMOB_AlwaysOffset"
