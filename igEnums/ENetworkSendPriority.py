# ENetworkSendPriority.py

from enum import Enum

class ENetworkSendPriority(Enum):
    eNSP_Low = "eNSP_Low"
    eNSP_Normal = "eNSP_Normal"
    eNSP_High = "eNSP_High"
    eNSP_Critical = "eNSP_Critical"
