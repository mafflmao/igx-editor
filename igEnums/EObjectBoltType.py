# EObjectBoltType.py

from enum import Enum

class EObjectBoltType(Enum):
    eOBT_INVALID = "eOBT_INVALID"
    eOBT_WORLD = "eOBT_WORLD"
    eOBT_ENTITY = "eOBT_ENTITY"
    eOBT_GAME = "eOBT_GAME"
    eOBT_STATIC = "eOBT_STATIC"
    eOBT_CUTSCENE = "eOBT_CUTSCENE"
    eOBT_ACTOR = "eOBT_ACTOR"
    eOBT_MODEL = "eOBT_MODEL"
    eOBT_IGENTITY = "eOBT_IGENTITY"
    eOBT_COUNT = "eOBT_COUNT"
