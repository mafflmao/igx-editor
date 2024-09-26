# ESpawnPositionMode.py

from enum import Enum

class ESpawnPositionMode(Enum):
    eSPM_AbsoluteWorldSpace = "eSPM_AbsoluteWorldSpace"
    eSPM_WorldSpaceOffset = "eSPM_WorldSpaceOffset"
    eSPM_EntityLocalOffset = "eSPM_EntityLocalOffset"
    eSPM_BoltLocalOffset = "eSPM_BoltLocalOffset"
    eSPM_SpawnOrientationOffset = "eSPM_SpawnOrientationOffset"
