# EMagicMomentState.py

from enum import Enum

class EMagicMomentState(Enum):
    eMMS_Inactive = "eMMS_Inactive"
    eMMS_Activating = "eMMS_Activating"
    eMMS_SpawnOutLevel = "eMMS_SpawnOutLevel"
    eMMS_TransitionIn = "eMMS_TransitionIn"
    eMMS_BossEvent = "eMMS_BossEvent"
    eMMS_Idle = "eMMS_Idle"
    eMMS_ConfirmRegister = "eMMS_ConfirmRegister"
    eMMS_FirstVehicleSequence = "eMMS_FirstVehicleSequence"
    eMMS_IdleOutro = "eMMS_IdleOutro"
    eMMS_Load = "eMMS_Load"
    eMMS_SpawnShapeshifter = "eMMS_SpawnShapeshifter"
    eMMS_PlayIntro = "eMMS_PlayIntro"
    eMMS_TransitionOut = "eMMS_TransitionOut"
    eMMS_SpawnInLevel = "eMMS_SpawnInLevel"
    eMMS_Dead = "eMMS_Dead"
    eMMS_PvPDead = "eMMS_PvPDead"
    eMMS_PvPVictory = "eMMS_PvPVictory"
    eMMS_Error = "eMMS_Error"
    eMMS_OnlineIntro = "eMMS_OnlineIntro"
    eMMS_OnlineOutro = "eMMS_OnlineOutro"
    eMMS_OnlineOutroConfirm = "eMMS_OnlineOutroConfirm"
    eMMS_OnlineWaitForHeroes = "eMMS_OnlineWaitForHeroes"
