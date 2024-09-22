# EDamageType.py

from enum import Enum

class EDamageType(Enum):
    eDMG_None = "eDMG_None"
    eDMG_Basic = "eDMG_Basic"
    eDMG_Poison = "eDMG_Poison"
    eDMG_Water = "eDMG_Water"
    eDMG_Fire = "eDMG_Fire"
    eDMG_Air = "eDMG_Air"
    eDMG_Electricity = "eDMG_Electricity"
    eDMG_Crushing = "eDMG_Crushing"
    eDMG_Magic = "eDMG_Magic"
    eDMG_Blade = "eDMG_Blade"
    eDMG_Victim = "eDMG_Victim"
    eDMG_Max = "eDMG_Max"