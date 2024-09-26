# ENetworkSyncWaitMode.py

from enum import Enum

class ENetworkSyncWaitMode(Enum):
    eNSWM_None = "eNSWM_None"
    eNSWM_SyncWait = "eNSWM_SyncWait"
    eNSWM_SyncWaitForUi = "eNSWM_SyncWaitForUi"
