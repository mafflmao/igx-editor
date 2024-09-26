# ESplineMoverEventAlert.py

from enum import Enum

class ESplineMoverEventAlert(Enum):
    eSMEA_None = "eSMEA_None"
    eSMEA_Started = "eSMEA_Started"
    eSMEA_Ended = "eSMEA_Ended"
    eSMEA_EventFired = "eSMEA_EventFired"
    eSMEA_Detached = "eSMEA_Detached"
