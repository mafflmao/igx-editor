# ESpellTargets.py

from enum import Enum

class ESpellTargets(Enum):
    eST_NONE = "eST_NONE"
    eST_START = "eST_START"
    eST_Player = "eST_Player"
    eST_BoardSlot0 = "eST_BoardSlot0"
    eST_BoardSlot1 = "eST_BoardSlot1"
    eST_BoardSlot2 = "eST_BoardSlot2"
    eST_HandIndex0 = "eST_HandIndex0"
    eST_HandIndex1 = "eST_HandIndex1"
    eST_HandIndex2 = "eST_HandIndex2"
    eST_END = "eST_END"
    eST_BoardAny = "eST_BoardAny"
    eST_HandAny = "eST_HandAny"
    eST_AnyCardSlot = "eST_AnyCardSlot"
