# EVehicleStatSource.py

from enum import Enum

class EVehicleStatSource(Enum):
    eVSS_Invalid = "eVSS_Invalid"
    eVSS_Start = "eVSS_Start"
    eVSS_Base = "eVSS_Base"
    eVSS_Variant = "eVSS_Variant"
    eVSS_PrimaryMod = "eVSS_PrimaryMod"
    eVSS_SecondaryMod = "eVSS_SecondaryMod"
    eVSS_UpgradeBoost = "eVSS_UpgradeBoost"
    eVSS_SuperchargeBoost = "eVSS_SuperchargeBoost"
    eVSS_TemporaryBoost = "eVSS_TemporaryBoost"
    eVSS_VehicleState = "eVSS_VehicleState"
    eVSS_Count = "eVSS_Count"
