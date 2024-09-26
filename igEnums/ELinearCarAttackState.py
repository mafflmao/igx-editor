# ELinearCarAttackState.py

from enum import Enum

class ELinearCarAttackState(Enum):
    eLCAS_NotAttacking = "eLCAS_NotAttacking"
    eLCAS_Telegraphing = "eLCAS_Telegraphing"
    eLCAS_Attacking = "eLCAS_Attacking"
