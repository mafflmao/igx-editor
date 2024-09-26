# EDataSortMethod.py

from enum import Enum

class EDataSortMethod(Enum):
    eDSM_None = "eDSM_None"
    eDSM_ClosestToFarthest = "eDSM_ClosestToFarthest"
    eDSM_FarthestToClosest = "eDSM_FarthestToClosest"
    eDSM_MostHealthToLeast = "eDSM_MostHealthToLeast"
    eDSM_LeastHealthToMost = "eDSM_LeastHealthToMost"
    eDSM_LeftToRight = "eDSM_LeftToRight"
    eDSM_RightToLeft = "eDSM_RightToLeft"
