# EEntitySpawnAuthority.py

from enum import Enum

class EEntitySpawnAuthority(Enum):
    eESA_LocalAuthority = "eESA_LocalAuthority"
    eESA_HostAuthority = "eESA_HostAuthority"
    eESA_NoAuthority = "eESA_NoAuthority"
    eESA_ParentAuthority = "eESA_ParentAuthority"
    eESA_Targetting = "eESA_Targetting"
    eESA_AiTacticalUpdate = "eESA_AiTacticalUpdate"
    eESA_WheelVisual = "eESA_WheelVisual"
    eESA_AiSensorsUpdate = "eESA_AiSensorsUpdate"
    eESA_AiCachedMaxSpeed = "eESA_AiCachedMaxSpeed"
    eESA_AiCachedTurnSpeed = "eESA_AiCachedTurnSpeed"
    eESA_AiCachedVehicleWeight = "eESA_AiCachedVehicleWeight"
    eESA_AudioComponentUpdate = "eESA_AudioComponentUpdate"
    eESA_AiVehicleStatsModifiers = "eESA_AiVehicleStatsModifiers"
    eESA_Count = "eESA_Count"
