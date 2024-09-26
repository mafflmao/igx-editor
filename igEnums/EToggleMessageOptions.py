# EToggleMessageOptions.py

from enum import Enum

class EToggleMessageOptions(Enum):
    eTMO_Activate = "eTMO_Activate"
    eTMO_PauseImmediately = "eTMO_PauseImmediately"
    eTMO_PauseAtNextWaypoint = "eTMO_PauseAtNextWaypoint"
    eTMO_Unpause = "eTMO_Unpause"
    eTMO_Deactivate = "eTMO_Deactivate"
