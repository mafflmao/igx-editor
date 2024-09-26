# ETouchHandlingMode.py

from enum import Enum

class ETouchHandlingMode(Enum):
    eTHM_None = "eTHM_None"
    eTHM_Focus = "eTHM_Focus"
    eTHM_FocusThenSelect = "eTHM_FocusThenSelect"
    eTHM_FocusAndSelect = "eTHM_FocusAndSelect"
