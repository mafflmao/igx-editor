# ESoundPauseType.py

from enum import Enum

class ESoundPauseType(Enum):
    eSPT_InGame = "eSPT_InGame"
    eSPT_Dialog = "eSPT_Dialog"
    eSPT_MagicMoment = "eSPT_MagicMoment"
    eSPT_PauseMenu = "eSPT_PauseMenu"
    eSPT_AllPaused = "eSPT_AllPaused"
