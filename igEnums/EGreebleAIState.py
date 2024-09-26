# EGreebleAIState.py

from enum import Enum

class EGreebleAIState(Enum):
    eGAIS_Unaware = "eGAIS_Unaware"
    eGAIS_AcquireTarget = "eGAIS_AcquireTarget"
    eGAIS_ApproachDestination = "eGAIS_ApproachDestination"
    eGAIS_Attack = "eGAIS_Attack"
    eGAIS_AttackWait = "eGAIS_AttackWait"
    eGAIS_AttackStrafe = "eGAIS_AttackStrafe"
    eGAIS_AttackBackOff = "eGAIS_AttackBackOff"
    eGAIS_Standby = "eGAIS_Standby"
    eGAIS_Taunt = "eGAIS_Taunt"
    eGAIS_Foiled = "eGAIS_Foiled"
    eGAIS_Immobilized = "eGAIS_Immobilized"
    eGAIS_TargetFound = "eGAIS_TargetFound"
    eGAIS_Jumping = "eGAIS_Jumping"
    eGAIS_FaceTarget = "eGAIS_FaceTarget"
    eGAIS_WalkThroughBorder = "eGAIS_WalkThroughBorder"
