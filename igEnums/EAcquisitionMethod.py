# EAcquisitionMethod.py

from enum import Enum

class EAcquisitionMethod(Enum):
    eAM_RandomDrop = "eAM_RandomDrop"
    eAM_InitiallyAvailable = "eAM_InitiallyAvailable"
    eAM_SpecificallyAwarded = "eAM_SpecificallyAwarded"
    eAM_PlacedInLevel = "eAM_PlacedInLevel"
