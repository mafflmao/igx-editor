# EMagicMomentPlayIntroSubState.py

from enum import Enum

class EMagicMomentPlayIntroSubState(Enum):
    eMMPISS_None = "eMMPISS_None"
    eMMPISS_VehicleIntro = "eMMPISS_VehicleIntro"
    eMMPISS_VehicleShowcase = "eMMPISS_VehicleShowcase"
    eMMPISS_VehicleWaitForPlayer = "eMMPISS_VehicleWaitForPlayer"
    eMMPISS_DriverJumpIn = "eMMPISS_DriverJumpIn"
    eMMPISS_SuperCharge = "eMMPISS_SuperCharge"
    eMMPISS_CharacterIntro = "eMMPISS_CharacterIntro"
    eMMPISS_ShortCharacterIntro = "eMMPISS_ShortCharacterIntro"
    eMMPISS_ExitVehicle = "eMMPISS_ExitVehicle"
    eMMPISS_ExitOnFoot = "eMMPISS_ExitOnFoot"
    eMMPISS_CoopWaitForOtherPlayer = "eMMPISS_CoopWaitForOtherPlayer"
