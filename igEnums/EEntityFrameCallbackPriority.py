# EEntityFrameCallbackPriority.py

from enum import Enum

class EEntityFrameCallbackPriority(Enum):
    eEFCP_First = "eEFCP_First"
    eEFCP_StartComponents = "eEFCP_StartComponents"
    eEFCP_UpdateDelegates = "eEFCP_UpdateDelegates"
    eEFCP_Default = "eEFCP_Default"
    eEFCP_RemoveComponents = "eEFCP_RemoveComponents"
    eEFCP_Last = "eEFCP_Last"
