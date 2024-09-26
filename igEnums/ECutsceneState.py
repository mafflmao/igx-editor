# ECutsceneState.py

from enum import Enum

class ECutsceneState(Enum):
    eCS_Idle = "eCS_Idle"
    eCS_Preparing = "eCS_Preparing"
    eCS_Playing = "eCS_Playing"
    eCS_Done = "eCS_Done"
