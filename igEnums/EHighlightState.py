# EHighlightState.py

from enum import Enum

class EHighlightState(Enum):
    eHS_None = "eHS_None"
    eHS_IsWorld = "eHS_IsWorld"
    eHS_CanDropMod = "eHS_CanDropMod"
    eHS_DistanceCullImportance = "eHS_DistanceCullImportance"
