# ETouchStatus.py

from enum import Enum

class ETouchStatus(Enum):
    eTS_TouchedWithoutFocus = "eTS_TouchedWithoutFocus"
    eTS_TouchedWithFocus = "eTS_TouchedWithFocus"
    eTS_Idle = "eTS_Idle"
