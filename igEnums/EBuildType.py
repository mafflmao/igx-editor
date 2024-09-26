# EBuildType.py

from enum import Enum

class EBuildType(Enum):
    eBT_Status = "eBT_Status"
    eBT_Inactive = "eBT_Inactive"
    eBT_Idle = "eBT_Idle"
    eBT_Searching = "eBT_Searching"
    eBT_Evaluating = "eBT_Evaluating"
    eBT_Hosting = "eBT_Hosting"
    eBT_Joining = "eBT_Joining"
    eBT_Connected = "eBT_Connected"
