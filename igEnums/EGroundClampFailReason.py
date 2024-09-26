# EGroundClampFailReason.py

from enum import Enum

class EGroundClampFailReason(Enum):
    eGCFR_FirstFail = "eGCFR_FirstFail"
    eGCFR_Fail = "eGCFR_Fail"
    eGCFR_FailEnded = "eGCFR_FailEnded"
