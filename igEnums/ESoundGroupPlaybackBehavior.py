# ESoundGroupPlaybackBehavior.py

from enum import Enum

class ESoundGroupPlaybackBehavior(Enum):
    eSGPB_Fail = "eSGPB_Fail"
    eSGPB_Mute = "eSGPB_Mute"
    eSGPB_StealLowest = "eSGPB_StealLowest"
