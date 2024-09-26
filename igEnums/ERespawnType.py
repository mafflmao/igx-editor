# ERespawnType.py

from enum import Enum

class ERespawnType(Enum):
    eRT_RespawnTrigger = "eRT_RespawnTrigger"
    eRT_InstantRespawnTrigger = "eRT_InstantRespawnTrigger"
    eRT_WaterRespawnTrigger = "eRT_WaterRespawnTrigger"
    eRT_IceRespawnTrigger = "eRT_IceRespawnTrigger"
    eRT_KillZ = "eRT_KillZ"
    eRT_Instant = "eRT_Instant"
    eRT_PVPDeathDelayed = "eRT_PVPDeathDelayed"
    eRT_Unknown = "eRT_Unknown"
