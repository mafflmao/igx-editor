# EBallotState.py

from enum import Enum

class EBallotState(Enum):
    eBS_Reset = "eBS_Reset"
    eBS_Ready = "eBS_Ready"
    eBS_AcknowledgeEveryoneReady = "eBS_AcknowledgeEveryoneReady"
    eBS_Max = "eBS_Max"
