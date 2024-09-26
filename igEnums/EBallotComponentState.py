# EBallotComponentState.py

from enum import Enum

class EBallotComponentState(Enum):
    eBCS_WaitingForPlayers = "eBCS_WaitingForPlayers"
    eBCS_EveryoneReady = "eBCS_EveryoneReady"
    eBCS_Reset = "eBCS_Reset"
    eBCS_Max = "eBCS_Max"
