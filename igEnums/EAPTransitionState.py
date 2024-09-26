# EAPTransitionState.py

from enum import Enum

class EAPTransitionState(Enum):
    eAPTS_Inactive = "eAPTS_Inactive"
    eAPTS_SectionInitialization = "eAPTS_SectionInitialization"
    eAPTS_Active = "eAPTS_Active"
    eAPTS_Idle = "eAPTS_Idle"
