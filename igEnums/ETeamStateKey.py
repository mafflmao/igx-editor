# ETeamStateKey.py

from enum import Enum

class ETeamStateKey(Enum):
    eTSK_Invalid = "eTSK_Invalid"
    eTSK_Begin = "eTSK_Begin"
    eTSK_FlagCaptures = "eTSK_FlagCaptures"
    eTSK_AIKills = "eTSK_AIKills"
    eTSK_PlayerKills = "eTSK_PlayerKills"
    eTSK_PlayerDeaths = "eTSK_PlayerDeaths"
    eTSK_MapSpecific1 = "eTSK_MapSpecific1"
    eTSK_MapSpecific2 = "eTSK_MapSpecific2"
    eTSK_MapSpecific3 = "eTSK_MapSpecific3"
    eTSK_MapSpecific4 = "eTSK_MapSpecific4"
    eTSK_Max = "eTSK_Max"
