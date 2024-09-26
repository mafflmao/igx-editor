# ESimulationMode.py

from enum import Enum

class ESimulationMode(Enum):
    eSM_None = "eSM_None"
    eSM_Best = "eSM_Best"
    eSM_Mean = "eSM_Mean"
    eSM_Worst = "eSM_Worst"
    eSM_Intermittent = "eSM_Intermittent"
    eSM_Custom = "eSM_Custom"
