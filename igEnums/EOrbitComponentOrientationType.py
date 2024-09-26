# EOrbitComponentOrientationType.py

from enum import Enum

class EOrbitComponentOrientationType(Enum):
    eOCOT_DoNotOrient = "eOCOT_DoNotOrient"
    eOCOT_Spin = "eOCOT_Spin"
    eOCOT_FaceOrbitAroundEntity = "eOCOT_FaceOrbitAroundEntity"
    eOCOT_FaceDirectionOfOrbitAroundEntity = "eOCOT_FaceDirectionOfOrbitAroundEntity"
    eOCOT_FaceDirectionOfOrbit = "eOCOT_FaceDirectionOfOrbit"
