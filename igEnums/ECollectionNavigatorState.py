# ECollectionNavigatorState.py

from enum import Enum

class ECollectionNavigatorState(Enum):
    eCNS_Normal = "eCNS_Normal"
    eCNS_MultiLevel = "eCNS_MultiLevel"
    eCNS_XAxis = "eCNS_XAxis"
    eCNS_YAxis = "eCNS_YAxis"
    eCNS_ZAxis = "eCNS_ZAxis"
    eCNS_Position = "eCNS_Position"
    eCNS_Velocity = "eCNS_Velocity"
