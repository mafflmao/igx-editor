# EFlyingAIState.py

from enum import Enum

class EFlyingAIState(Enum):
    eFAIS_Nothing = "eFAIS_Nothing"
    eFAIS_ChooseRandomDestination = "eFAIS_ChooseRandomDestination"
    eFAIS_ApproachDestination = "eFAIS_ApproachDestination"
    eFAIS_LineUpWithTarget = "eFAIS_LineUpWithTarget"
    eFAIS_AttackTarget = "eFAIS_AttackTarget"
    eFAIS_Chase = "eFAIS_Chase"
