# EAirVehicleForwardMovementState.py

from enum import Enum

class EAirVehicleForwardMovementState(Enum):
    eAVFMS_Idle = "eAVFMS_Idle"
    eAVFMS_Accelerating = "eAVFMS_Accelerating"
    eAVFMS_Reverting = "eAVFMS_Reverting"
    eAVFMS_Breaking = "eAVFMS_Breaking"
