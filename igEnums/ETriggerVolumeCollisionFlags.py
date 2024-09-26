# ETriggerVolumeCollisionFlags.py

from enum import Enum

class ETriggerVolumeCollisionFlags(Enum):
    eTVCF_TeamHero = "eTVCF_TeamHero"
    eTVCF_Players = "eTVCF_Players"
    eTVCF_NpcNeutral = "eTVCF_NpcNeutral"
    eTVCF_NpcEnemy = "eTVCF_NpcEnemy"
    eTVCF_NpcAltEnemy = "eTVCF_NpcAltEnemy"
    eTVCF_Projectile = "eTVCF_Projectile"
    eTVCF_Debris = "eTVCF_Debris"
    eTVCF_World = "eTVCF_World"
    eTVCF_LevelBorder = "eTVCF_LevelBorder"
    eTVCF_Damageable = "eTVCF_Damageable"
