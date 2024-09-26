# EPortalErrorType.py

from enum import Enum

class EPortalErrorType(Enum):
    ePET_Disconnect = "ePET_Disconnect"
    ePET_TooMany = "ePET_TooMany"
    ePET_Version = "ePET_Version"
    ePET_InvalidToy = "ePET_InvalidToy"
