# EVehicleReticleState.py

from enum import Enum

class EVehicleReticleState(Enum):
    eVRS_Hidden = "eVRS_Hidden"
    eVRS_Shown = "eVRS_Shown"
    eVRS_FiringBeginning = "eVRS_FiringBeginning"
    eVRS_FiringFinished = "eVRS_FiringFinished"
