# EScaleMode.py

from enum import Enum

class EScaleMode(Enum):
    eSM_NoScaling = "eSM_NoScaling"
    eSM_ScaleCollisionOnSpawnOnly = "eSM_ScaleCollisionOnSpawnOnly"
    eSM_ScaleCollisionWhenChanged = "eSM_ScaleCollisionWhenChanged"
