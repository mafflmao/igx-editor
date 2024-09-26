# EHavokQueryKillReason.py

from enum import Enum

class EHavokQueryKillReason(Enum):
    eHQKR_Unknown = "eHQKR_Unknown"
    eHQKR_InvalidSetup = "eHQKR_InvalidSetup"
    eHQKR_InvalidSource = "eHQKR_InvalidSource"
    eHQKR_InvalidTarget = "eHQKR_InvalidTarget"
    eHQKR_InvalidFilter = "eHQKR_InvalidFilter"
    eHQKR_OutOfSpace = "eHQKR_OutOfSpace"
    eHQKR_AutoCleanup = "eHQKR_AutoCleanup"
    eHQKR_ManualKill = "eHQKR_ManualKill"
    eHQKR_KillAll = "eHQKR_KillAll"
