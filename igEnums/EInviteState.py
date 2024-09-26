# EInviteState.py

from enum import Enum

class EInviteState(Enum):
    eIS_LobbyUp = "eIS_LobbyUp"
    eIS_LobbyDown = "eIS_LobbyDown"
    eIS_SignOut = "eIS_SignOut"
    eIS_FriendJoinable = "eIS_FriendJoinable"
    eIS_InviteReceived = "eIS_InviteReceived"
    eIS_PeerJoining = "eIS_PeerJoining"
    eIS_PeerDisconnected = "eIS_PeerDisconnected"
    eIS_HostDisconnected = "eIS_HostDisconnected"
