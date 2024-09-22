# EBeamBoltType.py

from enum import Enum

class EBeamBoltType(Enum):
    eBBT_None = "eBBT_None"
    eBBT_Self = "eBBT_Self"
    eBBT_SelfToCombatTarget = "eBBT_SelfToCombatTarget"
    eBBT_SelfToDummyEntity = "eBBT_SelfToDummyEntity"
    eBBT_SelfToAimedPosition = "eBBT_SelfToAimedPosition"