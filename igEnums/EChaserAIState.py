# EChaserAIState.py

from enum import Enum

class EChaserAIState(Enum):
    eCAIS_Unaware = "eCAIS_Unaware"
    eCAIS_Approaching = "eCAIS_Approaching"
    eCAIS_Circling = "eCAIS_Circling"
    eCAIS_FaceTarget = "eCAIS_FaceTarget"
    eCAIS_Telegraph = "eCAIS_Telegraph"
    eCAIS_Attacking = "eCAIS_Attacking"
    eCAIS_AttackEnd = "eCAIS_AttackEnd"
    eCAIS_InAir = "eCAIS_InAir"
    eCAIS_CancelAttack = "eCAIS_CancelAttack"
    eCAIS_NONE = "eCAIS_NONE"
    eCAIS_FAILURE = "eCAIS_FAILURE"
    eCAIS_CANCELLED = "eCAIS_CANCELLED"
    eCAIS_INSUFFICENT = "eCAIS_INSUFFICENT"
