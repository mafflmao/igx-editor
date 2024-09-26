# ESplineEndBehavior.py

from enum import Enum

class ESplineEndBehavior(Enum):
    eSEB_None = "eSEB_None"
    eSEB_Wrap = "eSEB_Wrap"
    eSEB_PingPong = "eSEB_PingPong"
    eSEB_KillEntity = "eSEB_KillEntity"
