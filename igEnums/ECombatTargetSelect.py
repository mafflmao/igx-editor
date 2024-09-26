# ECombatTargetSelect.py

from enum import Enum

class ECombatTargetSelect(Enum):
    eCTS_None = "eCTS_None"
    eCTS_Self = "eCTS_Self"
    eCTS_First = "eCTS_First"
    eCTS_Last = "eCTS_Last"
    eCTS_Owner = "eCTS_Owner"
    eCTS_PlayerControlledHero = "eCTS_PlayerControlledHero"
    eCTS_All = "eCTS_All"
