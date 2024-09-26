# EVehicleDockingEffectState.py

from enum import Enum

class EVehicleDockingEffectState(Enum):
    eVDES_None = "eVDES_None"
    eVDES_Beacon = "eVDES_Beacon"
    eVDES_PromptForCorrectVehicle = "eVDES_PromptForCorrectVehicle"
    eVDES_VehicleEnter = "eVDES_VehicleEnter"
    eVDES_VehicleExit = "eVDES_VehicleExit"
