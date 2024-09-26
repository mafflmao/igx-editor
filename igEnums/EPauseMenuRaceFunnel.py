# EPauseMenuRaceFunnel.py

from enum import Enum

class EPauseMenuRaceFunnel(Enum):
    ePMRF_AtPauseMenu = "ePMRF_AtPauseMenu"
    ePMRF_AtPauseMenuWithRacingAvailable = "ePMRF_AtPauseMenuWithRacingAvailable"
    ePMRF_AtBaseRacingMenu = "ePMRF_AtBaseRacingMenu"
    ePMRF_AttemptToEnterLobby = "ePMRF_AttemptToEnterLobby"
    ePMRF_InLobby = "ePMRF_InLobby"
    ePMRF_Searching = "ePMRF_Searching"
    ePMRF_StartRace = "ePMRF_StartRace"
