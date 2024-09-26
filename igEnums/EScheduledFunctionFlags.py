# EScheduledFunctionFlags.py

from enum import Enum

class EScheduledFunctionFlags(Enum):
    eSFF_None = "eSFF_None"
    eSFF_Loop = "eSFF_Loop"
    eSFF_TimeAsFrames = "eSFF_TimeAsFrames"
    eSFF_IgnoreGamePause = "eSFF_IgnoreGamePause"
    eSFF_IgnoreGameSlomo = "eSFF_IgnoreGameSlomo"
    eSFF_Paused = "eSFF_Paused"
    eSFF_Stopped = "eSFF_Stopped"
    eSFF_Running = "eSFF_Running"
    eSFF_RunOnCleanup = "eSFF_RunOnCleanup"
