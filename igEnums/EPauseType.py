# EPauseType.py

from enum import Enum

class EPauseType(Enum):
    ePT_Game = "ePT_Game"
    ePT_Cutscene = "ePT_Cutscene"
    ePT_Remote = "ePT_Remote"
    ePT_SystemUI = "ePT_SystemUI"
    ePT_Default = "ePT_Default"
