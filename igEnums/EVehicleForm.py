# EVehicleForm.py

from enum import Enum

class EVehicleForm(Enum):
    eVF_None = "eVF_None"
    eVF_Invisible = "eVF_Invisible"
    eVF_Spawning = "eVF_Spawning"
    eVF_Parked = "eVF_Parked"
    eVF_UnDocking = "eVF_UnDocking"
    eVF_Driving = "eVF_Driving"
    eVF_Docking = "eVF_Docking"
    eVF_Disembarking = "eVF_Disembarking"
    eVF_ExitingTrack = "eVF_ExitingTrack"
