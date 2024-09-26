# EGuiContext.py

from enum import Enum

class EGuiContext(Enum):
    eGC_Invalid = "eGC_Invalid"
    eGC_Main = "eGC_Main"
    eGC_Minigame = "eGC_Minigame"
    eGC_Loading = "eGC_Loading"
    eGC_MagicMoment = "eGC_MagicMoment"
    eGC_Movie = "eGC_Movie"
    eGC_Subscreen = "eGC_Subscreen"
    eGC_Max = "eGC_Max"
