# ELinearCarAIState.py

from enum import Enum

class ELinearCarAIState(Enum):
    eLCAIS_Inactive = "eLCAIS_Inactive"
    eLCAIS_CatchUp = "eLCAIS_CatchUp"
    eLCAIS_TrackTarget = "eLCAIS_TrackTarget"
    eLCAIS_WaitAhead = "eLCAIS_WaitAhead"
    eLCAIS_PrepareCharge = "eLCAIS_PrepareCharge"
    eLCAIS_Charge = "eLCAIS_Charge"
    eLCAIS_ChargeEnd = "eLCAIS_ChargeEnd"
