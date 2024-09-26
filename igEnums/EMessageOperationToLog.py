# EMessageOperationToLog.py

from enum import Enum

class EMessageOperationToLog(Enum):
    eMOTL_None = "eMOTL_None"
    eMOTL_Queued = "eMOTL_Queued"
    eMOTL_Received = "eMOTL_Received"
    eMOTL_SentImmediately = "eMOTL_SentImmediately"
