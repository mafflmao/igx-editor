# ETargetArrowMode.py

from enum import Enum

class ETargetArrowMode(Enum):
    eTAM_Disabled = "eTAM_Disabled"
    eTAM_SingleTarget = "eTAM_SingleTarget"
    eTAM_MultipleTargets = "eTAM_MultipleTargets"
    eTAM_ClampFacing = "eTAM_ClampFacing"
    eTAM_ClampGlancing = "eTAM_ClampGlancing"
    eTAM_ClampPeak = "eTAM_ClampPeak"
