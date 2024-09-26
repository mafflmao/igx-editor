# EEntityDataFlags.py

from enum import Enum

class EEntityDataFlags(Enum):
    eEDF_None = "eEDF_None"
    eEDF_NoGravity = "eEDF_NoGravity"
    eEDF_IsWorld = "eEDF_IsWorld"
    eEDF_NoCollision = "eEDF_NoCollision"
    eEDF_NoPush = "eEDF_NoPush"
    eEDF_NoDifficultyAdjust = "eEDF_NoDifficultyAdjust"
    eEDF_NoClip = "eEDF_NoClip"
    eEDF_RemoveOnCutscene = "eEDF_RemoveOnCutscene"
    eEDF_StopTeamHero = "eEDF_StopTeamHero"
    eEDF_StopNPCNeutral = "eEDF_StopNPCNeutral"
    eEDF_StopNPCEnemy = "eEDF_StopNPCEnemy"
    eEDF_StopNPCAltEnemy = "eEDF_StopNPCAltEnemy"
    eEDF_StopProjectile = "eEDF_StopProjectile"
    eEDF_StopDebris = "eEDF_StopDebris"
    eEDF_StopWorld = "eEDF_StopWorld"
    eEDF_Targetable = "eEDF_Targetable"
    eEDF_NetReplicate = "eEDF_NetReplicate"
    eEDF_NetAuthorityCanMigrate = "eEDF_NetAuthorityCanMigrate"
    eEDF_NetLowPriority = "eEDF_NetLowPriority"
    eEDF_NetAlwaysOfInterest = "eEDF_NetAlwaysOfInterest"
    eEDF_IsLevelBorder = "eEDF_IsLevelBorder"
    eEDF_StopPlayers = "eEDF_StopPlayers"
    eEDF_StopLevelBorder = "eEDF_StopLevelBorder"
