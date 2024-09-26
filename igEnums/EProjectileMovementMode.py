# EProjectileMovementMode.py

from enum import Enum

class EProjectileMovementMode(Enum):
    ePMM_StraightLine = "ePMM_StraightLine"
    ePMM_FollowGround = "ePMM_FollowGround"
    ePMM_Lobbed = "ePMM_Lobbed"
    ePMM_Homing = "ePMM_Homing"
    ePMM_HomingAvoidGround = "ePMM_HomingAvoidGround"
    ePMM_Physics = "ePMM_Physics"
    ePMM_HomingFollowGround = "ePMM_HomingFollowGround"
    ePMM_HomingFollowWallAndGround = "ePMM_HomingFollowWallAndGround"
    ePMM_AvoidGround = "ePMM_AvoidGround"
    ePMM_HomingPlanar = "ePMM_HomingPlanar"
