# EPlayerCancelAttackReason.py

from enum import Enum

class EPlayerCancelAttackReason(Enum):
    ePCAR_Jump = "ePCAR_Jump"
    ePCAR_LockedControls = "ePCAR_LockedControls"
    ePCAR_Respawn = "ePCAR_Respawn"
    ePCAR_HitReact = "ePCAR_HitReact"
    ePCAR_ReleasedButton = "ePCAR_ReleasedButton"
    ePCAR_ActorInVehicle = "ePCAR_ActorInVehicle"
    ePCAR_TriggeredOtherAttack = "ePCAR_TriggeredOtherAttack"
    ePCAR_DisabledRacing = "ePCAR_DisabledRacing"
    ePCAR_NetForceLocomotion = "ePCAR_NetForceLocomotion"
    ePCAR_Other = "ePCAR_Other"
