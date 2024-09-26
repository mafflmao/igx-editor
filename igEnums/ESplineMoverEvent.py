# ESplineMoverEvent.py

from enum import Enum

class ESplineMoverEvent(Enum):
    eSME_Play = "eSME_Play"
    eSME_Reverse = "eSME_Reverse"
    eSME_Pause = "eSME_Pause"
    eSME_Stop = "eSME_Stop"
    eSME_Loop = "eSME_Loop"
    eSME_PingPong = "eSME_PingPong"
    eSME_JumpToBeginning = "eSME_JumpToBeginning"
    eSME_JumpToEnd = "eSME_JumpToEnd"
    eSME_JumpToRatio = "eSME_JumpToRatio"
    eSME_PlayForward = "eSME_PlayForward"
    eSME_PlayBackward = "eSME_PlayBackward"
    eSME_SetVelocity = "eSME_SetVelocity"
    eSME_GotoDestinationEvent = "eSME_GotoDestinationEvent"
    eSME_Attach = "eSME_Attach"
    eSME_AttachAndPlay = "eSME_AttachAndPlay"
    eSME_ReattachAndPlay = "eSME_ReattachAndPlay"
    eSME_UpdateTrackToRatio = "eSME_UpdateTrackToRatio"
