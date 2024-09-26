# EDebugDrawEffectType.py

from enum import Enum

class EDebugDrawEffectType(Enum):
    eDDET_None = "eDDET_None"
    eDDET_Active = "eDDET_Active"
    eDDET_Instances = "eDDET_Instances"
    eDDET_All = "eDDET_All"
    eDDET_NovaRecentlySpawned = "eDDET_NovaRecentlySpawned"
    eDDET_AllRecentlySpawned = "eDDET_AllRecentlySpawned"
    eDDET_WorstOffenders = "eDDET_WorstOffenders"
    eDDET_Deprioritized = "eDDET_Deprioritized"
    eDDET_Count = "eDDET_Count"
    eDDET_ToPartType = "eDDET_ToPartType"
    eDDET_ReturnToGameCamera = "eDDET_ReturnToGameCamera"
