# EAimingMethod.py

from enum import Enum

class EAimingMethod(Enum):
    eAM_NoAiming = "eAM_NoAiming"
    eAM_AimAtTarget = "eAM_AimAtTarget"
    eAM_AimAtAimedPosition = "eAM_AimAtAimedPosition"
    eAM_AimAtTargetThenPosition = "eAM_AimAtTargetThenPosition"
    eAM_LeadTarget = "eAM_LeadTarget"
