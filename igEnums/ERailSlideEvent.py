# ERailSlideEvent.py

from enum import Enum

class ERailSlideEvent(Enum):
    eRSE_JumpUp = "eRSE_JumpUp"
    eRSE_JumpLeft = "eRSE_JumpLeft"
    eRSE_JumpRight = "eRSE_JumpRight"
    eRSE_Cancelled = "eRSE_Cancelled"
    eRSE_Success = "eRSE_Success"
    eRSE_Failure = "eRSE_Failure"
