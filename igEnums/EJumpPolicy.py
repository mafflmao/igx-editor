# EJumpPolicy.py

from enum import Enum

class EJumpPolicy(Enum):
    eJP_Allowed = "eJP_Allowed"
    eJP_NotAllowed = "eJP_NotAllowed"
    eJP_Forced = "eJP_Forced"
    eJP_ForceSnapLeft = "eJP_ForceSnapLeft"
    eJP_ForceSnapRight = "eJP_ForceSnapRight"
