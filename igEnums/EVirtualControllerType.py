# EVirtualControllerType.py

from enum import Enum

class EVirtualControllerType(Enum):
    eVCT_None = "eVCT_None"
    eVCT_OnFoot = "eVCT_OnFoot"
    eVCT_Land = "eVCT_Land"
    eVCT_Sea = "eVCT_Sea"
    eVCT_Air = "eVCT_Air"
    eVCT_Max = "eVCT_Max"
