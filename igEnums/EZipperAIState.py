# EZipperAIState.py

from enum import Enum

class EZipperAIState(Enum):
    eZAIS_ChoosePatrolPoint = "eZAIS_ChoosePatrolPoint"
    eZAIS_FlyToPatrolPoint = "eZAIS_FlyToPatrolPoint"
    eZAIS_PatrolWait = "eZAIS_PatrolWait"
    eZAIS_FlyToTargetPoint = "eZAIS_FlyToTargetPoint"
    eZAIS_FollowTarget = "eZAIS_FollowTarget"
    eZAIS_Reposition = "eZAIS_Reposition"
    eZAIS_AttackStart = "eZAIS_AttackStart"
    eZAIS_AttackLoop = "eZAIS_AttackLoop"
