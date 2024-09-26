# EEngagedEnemyDataFlags.py

from enum import Enum

class EEngagedEnemyDataFlags(Enum):
    eEEDF_None = "eEEDF_None"
    eEEDF_AttackPermission = "eEEDF_AttackPermission"
    eEEDF_AbleToAttack = "eEEDF_AbleToAttack"
    eEEDF_InInteriorCircle = "eEEDF_InInteriorCircle"
    eEEDF_NormalFromTargetValid = "eEEDF_NormalFromTargetValid"
    eEEDF_NeedsRefresh = "eEEDF_NeedsRefresh"
    eEEDF_MightMelee = "eEEDF_MightMelee"
