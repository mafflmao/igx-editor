# ENetworkSendRestriction.py

from enum import Enum

class ENetworkSendRestriction(Enum):
    eNSR_Local = "eNSR_Local"
    eNSR_FromAuthorityToAll = "eNSR_FromAuthorityToAll"
    eNSR_FromAuthorityToAllReliable = "eNSR_FromAuthorityToAllReliable"
    eNSR_FromCreatorAuthorityToAll = "eNSR_FromCreatorAuthorityToAll"
    eNSR_FromHostToAll = "eNSR_FromHostToAll"
    eNSR_FromHostToAllReliable = "eNSR_FromHostToAllReliable"
    eNSR_Broadcast = "eNSR_Broadcast"
    eNSR_BroadcastReliable = "eNSR_BroadcastReliable"
