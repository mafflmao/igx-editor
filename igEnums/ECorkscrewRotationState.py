# ECorkscrewRotationState.py

from enum import Enum

class ECorkscrewRotationState(Enum):
    eCRS_Stopped = "eCRS_Stopped"
    eCRS_PlayerMoving = "eCRS_PlayerMoving"
    eCRS_Decelerating = "eCRS_Decelerating"
    eCRS_RotatingToOriginalRotation = "eCRS_RotatingToOriginalRotation"
