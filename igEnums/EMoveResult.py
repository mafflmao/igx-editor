# EMoveResult.py

from enum import Enum

class EMoveResult(Enum):
    eMR_AtDestination = "eMR_AtDestination"
    eMR_PathImpossible = "eMR_PathImpossible"
    eMR_NotOnNavmesh = "eMR_NotOnNavmesh"
    eMR_Disabled = "eMR_Disabled"
    eMR_InfiniteLoop = "eMR_InfiniteLoop"
