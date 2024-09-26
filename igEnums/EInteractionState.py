# EInteractionState.py

from enum import Enum

class EInteractionState(Enum):
    eIS_Idle = "eIS_Idle"
    eIS_Alerted = "eIS_Alerted"
    eIS_NotInteractable = "eIS_NotInteractable"
    eIS_Interactable = "eIS_Interactable"
    eIS_Interacting = "eIS_Interacting"
    eIS_Interacted = "eIS_Interacted"
