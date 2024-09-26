# EPhysicalEntityDataFlags.py

from enum import Enum

class EPhysicalEntityDataFlags(Enum):
        ePEDF_None = "ePEDF_None"
        ePEDF_IgnoreActorsOnMove = "ePEDF_IgnoreActorsOnMove"
        ePEDF_IgnorePhantomsOnMove = "ePEDF_IgnorePhantomsOnMove"
        ePEDF_NoDamageNumbers = "ePEDF_NoDamageNumbers"
        ePEDF_Undying = "ePEDF_Undying"
        ePEDF_RemoveOnDeath = "ePEDF_RemoveOnDeath"
        ePEDF_IDealMoveDamage = "ePEDF_IDealMoveDamage"
        ePEDF_NoDifficultyHealthAdjust = "ePEDF_NoDifficultyHealthAdjust"