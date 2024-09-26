# EDeviceClass.py

from enum import Enum

class EDeviceClass(Enum):
    eDC_None = "eDC_None"
    eDC_Gen8Console = "eDC_Gen8Console"
    eDC_Gen7Console = "eDC_Gen7Console"
    eDC_HighTablet = "eDC_HighTablet"
    eDC_MediumTablet = "eDC_MediumTablet"
    eDC_LowTablet = "eDC_LowTablet"
