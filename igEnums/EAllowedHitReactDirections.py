# EAllowedHitReactDirections.py

from enum import Enum

class EAllowedHitReactDirections(Enum):
    eAHRD_NoReaction = "eAHRD_NoReaction"
    eAHRD_NoDirection = "eAHRD_NoDirection"
    eAHRD_Front = "eAHRD_Front"
    eAHRD_FrontAndBack = "eAHRD_FrontAndBack"
    eAHRD_FrontBackLeftRight = "eAHRD_FrontBackLeftRight"
