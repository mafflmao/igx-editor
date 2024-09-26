# EMoveMode.py

from enum import Enum

class EMoveMode(Enum):
    eMM_NavMover = "eMM_NavMover"
    eMM_NavMoverForceMove = "eMM_NavMoverForceMove"
    eMM_Direct = "eMM_Direct"
    eMM_Stop = "eMM_Stop"
