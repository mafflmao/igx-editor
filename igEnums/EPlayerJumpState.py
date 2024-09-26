# EPlayerJumpState.py

from enum import Enum

class EPlayerJumpState(Enum):
    ePJS_None = "ePJS_None"
    ePJS_JumpHold = "ePJS_JumpHold"
    ePJS_JumpRelease = "ePJS_JumpRelease"
    ePJS_Falling = "ePJS_Falling"
