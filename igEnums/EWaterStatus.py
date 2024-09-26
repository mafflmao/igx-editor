# EWaterStatus.py

from enum import Enum

class EWaterStatus(Enum):
    eWS_Unknown = "eWS_Unknown"
    eWS_AboveWater = "eWS_AboveWater"
    eWS_TouchingWater = "eWS_TouchingWater"
    eWS_UnderWater = "eWS_UnderWater"
