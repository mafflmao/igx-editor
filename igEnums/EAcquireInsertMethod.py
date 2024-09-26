# EAcquireInsertMethod.py

from enum import Enum

class EAcquireInsertMethod(Enum):
    eAIM_Clear = "eAIM_Clear"
    eAIM_Append = "eAIM_Append"
    eAIM_RemoveFront = "eAIM_RemoveFront"
    eAIM_RandomSwap = "eAIM_RandomSwap"
    eAIM_FilterCurrentList = "eAIM_FilterCurrentList"
