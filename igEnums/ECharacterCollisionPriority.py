# ECharacterCollisionPriority.py

from enum import Enum

class ECharacterCollisionPriority(Enum):
    eCCP_NonGameplayCritical = "eCCP_NonGameplayCritical"
    eCCP_None = "eCCP_None"
    eCCP_Low = "eCCP_Low"
    eCCP_NormalSelfPushable = "eCCP_NormalSelfPushable"
    eCCP_Normal = "eCCP_Normal"
    eCCP_JumpingPlayer = "eCCP_JumpingPlayer"
    eCCP_High = "eCCP_High"
    eCCP_Charger = "eCCP_Charger"
    eCCP_PlayerTraversable = "eCCP_PlayerTraversable"
    eCCP_Immobile = "eCCP_Immobile"
