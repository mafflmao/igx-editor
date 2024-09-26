# EEntityAttachmentFlags.py

from enum import Enum

class EEntityAttachmentFlags(Enum):
    eEAF_None = "eEAF_None"
    eEAF_PreserveOffset = "eEAF_PreserveOffset"
    eEAF_EnableCollision = "eEAF_EnableCollision"
    eEAF_MatchBolterScale = "eEAF_MatchBolterScale"
    eEAF_SingleFrame = "eEAF_SingleFrame"
    eEAF_KeepAngles = "eEAF_KeepAngles"
    eEAF_MatchBolterOverriddenScale = "eEAF_MatchBolterOverriddenScale"
    eEAF_NoCollide = "eEAF_NoCollide"
    eEAF_ForceNetReplicateDisable = "eEAF_ForceNetReplicateDisable"
    eEAF_UseBolterOverrideMatrix = "eEAF_UseBolterOverrideMatrix"
    eEAF_RefBoltPoint = "eEAF_RefBoltPoint"
