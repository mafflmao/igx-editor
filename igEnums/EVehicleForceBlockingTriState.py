# EVehicleForceBlockingTriState.py

from enum import Enum

class EVehicleForceBlockingTriState(Enum):
    eVFBTS_DefaultNotBlocking = "eVFBTS_DefaultNotBlocking"
    eVFBTS_DefaultBlocking = "eVFBTS_DefaultBlocking"
    eVFBTS_NeverBlocking = "eVFBTS_NeverBlocking"
    eVFBTS_ShockwaveWaveType = "eVFBTS_ShockwaveWaveType"
    eVFBTS_Invalid = "eVFBTS_Invalid"
    eVFBTS_Standard = "eVFBTS_Standard"
    eVFBTS_Tall = "eVFBTS_Tall"
    eVFBTS_Hazard = "eVFBTS_Hazard"
    eVFBTS_Unhazard = "eVFBTS_Unhazard"
