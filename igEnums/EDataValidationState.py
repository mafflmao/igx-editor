# EDataValidationState.py

from enum import Enum

class EDataValidationState(Enum):
    eDVS_Unchecked = "eDVS_Unchecked"
    eDVS_Valid = "eDVS_Valid"
    eDVS_Invalid = "eDVS_Invalid"
