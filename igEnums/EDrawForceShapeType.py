# EDrawForceShapeType.py

from enum import Enum

class EDrawForceShapeType(Enum):
    eDFST_Sphere = "eDFST_Sphere"
    eDFST_Box = "eDFST_Box"
    eDFST_NONE = "eDFST_NONE"
    eDFST_FAILURE = "eDFST_FAILURE"
    eDFST_ONCE = "eDFST_ONCE"
    eDFST_EVERY = "eDFST_EVERY"
