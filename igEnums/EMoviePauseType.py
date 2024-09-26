# EMoviePauseType.py

from enum import Enum

class EMoviePauseType(Enum):
    eMPT_None = "eMPT_None"
    eMPT_User = "eMPT_User"
    eMPT_SystemUI = "eMPT_SystemUI"
    eMPT_AfterLoad = "eMPT_AfterLoad"
