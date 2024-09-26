# EMainMenuRaceFunnel.py

from enum import Enum

class EMainMenuRaceFunnel(Enum):
    eMMRF_AtMainMenu = "eMMRF_AtMainMenu"
    eMMRF_AtMainMenuWithRacingAvailable = "eMMRF_AtMainMenuWithRacingAvailable"
    eMMRF_AtBaseRacingMenu = "eMMRF_AtBaseRacingMenu"
    eMMRF_AttemptToEnterLobby = "eMMRF_AttemptToEnterLobby"
    eMMRF_InLobby = "eMMRF_InLobby"
    eMMRF_Searching = "eMMRF_Searching"
    eMMRF_StartRace = "eMMRF_StartRace"
