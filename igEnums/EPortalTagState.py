# EPortalTagState.py

from enum import Enum

class EPortalTagState(Enum):
    ePTS_NotOnPortal = "ePTS_NotOnPortal"
    ePTS_IoWait = "ePTS_IoWait"
    ePTS_HeaderLoad = "ePTS_HeaderLoad"
    ePTS_HeaderReady = "ePTS_HeaderReady"
    ePTS_WaitForShapeshifterPair = "ePTS_WaitForShapeshifterPair"
    ePTS_MagicMomentLoad = "ePTS_MagicMomentLoad"
    ePTS_MagicMomentReady = "ePTS_MagicMomentReady"
    ePTS_RemainingLoad = "ePTS_RemainingLoad"
    ePTS_RemainingReady = "ePTS_RemainingReady"
    ePTS_OwnerIdLoad = "ePTS_OwnerIdLoad"
    ePTS_OwnerIdReady = "ePTS_OwnerIdReady"
    ePTS_VerifySecurity = "ePTS_VerifySecurity"
    ePTS_SecurityVerified = "ePTS_SecurityVerified"
    ePTS_Write = "ePTS_Write"
    ePTS_Reset = "ePTS_Reset"
    ePTS_OwnerIdReset = "ePTS_OwnerIdReset"
    ePTS_Recover = "ePTS_Recover"
    ePTS_WriteOwnerId = "ePTS_WriteOwnerId"
    ePTS_Idle = "ePTS_Idle"
    ePTS_SoftError = "ePTS_SoftError"
    ePTS_HardError = "ePTS_HardError"
