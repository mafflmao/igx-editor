# EHavokCollisionFlags.py

from enum import Enum

class EHavokCollisionFlags(Enum):
    eHCF_Nothing = "eHCF_Nothing"
    eHCF_TeamHero = "eHCF_TeamHero"
    eHCF_Players = "eHCF_Players"
    eHCF_NpcNeutral = "eHCF_NpcNeutral"
    eHCF_NpcEnemy = "eHCF_NpcEnemy"
    eHCF_NpcAltEnemy = "eHCF_NpcAltEnemy"
    eHCF_Projectile = "eHCF_Projectile"
    eHCF_Debris = "eHCF_Debris"
    eHCF_LevelBorder = "eHCF_LevelBorder"
    eHCF_World = "eHCF_World"
    eHCF_Damageable = "eHCF_Damageable"
    eHCF_Default = "eHCF_Default"
