# ESkylanderMinionAIState.py

from enum import Enum

class ESkylanderMinionAIState(Enum):
    eSMAIS_Idle = "eSMAIS_Idle"
    eSMAIS_MoveToAttack = "eSMAIS_MoveToAttack"
    eSMAIS_Attack = "eSMAIS_Attack"
    eSMAIS_MoveToIdle = "eSMAIS_MoveToIdle"
    eSMAIS_Explode = "eSMAIS_Explode"
    eSMAIS_Death = "eSMAIS_Death"
