# EOrientationActionType.py

from enum import Enum

class EOrientationActionType(Enum):
    eOAT_FaceTarget = "eOAT_FaceTarget"
    eOAT_FaceAwayFromTarget = "eOAT_FaceAwayFromTarget"
    eOAT_FaceTargetAngles = "eOAT_FaceTargetAngles"
    eOAT_FaceAwayFromCurrentDirection = "eOAT_FaceAwayFromCurrentDirection"
    eOAT_FaceInputDirection = "eOAT_FaceInputDirection"
    eOAT_FaceAwayFromCamera = "eOAT_FaceAwayFromCamera"
    eOAT_FaceCamera = "eOAT_FaceCamera"
