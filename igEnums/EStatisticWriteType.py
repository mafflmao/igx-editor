# EStatisticWriteType.py

from enum import Enum

class EStatisticWriteType(Enum):
    eSWT_Invalid = "eSWT_Invalid"
    eSWT_Replace = "eSWT_Replace"
    eSWT_Add = "eSWT_Add"
    eSWT_Max = "eSWT_Max"
    eSWT_Min = "eSWT_Min"
    eSWT_BitwiseOR = "eSWT_BitwiseOR"
