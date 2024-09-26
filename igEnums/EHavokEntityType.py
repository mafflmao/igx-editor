# EHavokEntityType.py

from enum import Enum

class EHavokEntityType(Enum):
    eHET_Undefined = "eHET_Undefined"
    eHET_Dynamic = "eHET_Dynamic"
    eHET_Fixed = "eHET_Fixed"
    eHET_Keyframed = "eHET_Keyframed"
    eHET_BehaviorController = "eHET_BehaviorController"
