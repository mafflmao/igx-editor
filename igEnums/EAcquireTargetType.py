# EAcquireTargetType.py

from enum import Enum

class EAcquireTargetType(Enum):
    eATT_None = "eATT_None"
    eATT_All = "eATT_All"
    eATT_EnemyActors = "eATT_EnemyActors"
    eATT_DynamicRigidBodies = "eATT_DynamicRigidBodies"
    eATT_HeroActors = "eATT_HeroActors"
    eATT_Self = "eATT_Self"
    eATT_CurrentCombatTargets = "eATT_CurrentCombatTargets"
    eATT_CurrentVictim = "eATT_CurrentVictim"
    eATT_PlayableHero = "eATT_PlayableHero"
