# EScriptTriggerFlags.py

from enum import Enum

class EScriptTriggerFlags(Enum):
    eSTF_None = "eSTF_None"
    eSTF_OnlyPlayersCanTrigger = "eSTF_OnlyPlayersCanTrigger"
    eSTF_SingleFire = "eSTF_SingleFire"
    eSTF_ProcessMagicMoment = "eSTF_ProcessMagicMoment"
    eSTF_AllowKeyframedEntities = "eSTF_AllowKeyframedEntities"
    eSTF_IsDirectional = "eSTF_IsDirectional"
