# ENavigationState.py

from enum import Enum

class ENavigationState(Enum):
    eNS_Idle = "eNS_Idle"
    eNS_Moving = "eNS_Moving"
    eNS_AtGoal = "eNS_AtGoal"
    eNS_Blocked = "eNS_Blocked"
    eNS_FollowingLink = "eNS_FollowingLink"
