# ERenderOverrideMode.py

from enum import Enum

class ERenderOverrideMode(Enum):
    eROM_None = "eROM_None"
    eROM_UseSavedWorld = "eROM_UseSavedWorld"
    eROM_StopRenderingWorld = "eROM_StopRenderingWorld"
    eROM_SaveWorld = "eROM_SaveWorld"
