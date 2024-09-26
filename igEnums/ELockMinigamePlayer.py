# ELockMinigamePlayer.py

from enum import Enum

class ELockMinigamePlayer(Enum):
    eLMP_One = "eLMP_One"
    eLMP_Two = "eLMP_Two"
    eLMP_Inactive = "eLMP_Inactive"
    eLMP_ReadyToStart = "eLMP_ReadyToStart"
    eLMP_FadingIn = "eLMP_FadingIn"
    eLMP_Active = "eLMP_Active"
    eLMP_StartFadeOut = "eLMP_StartFadeOut"
    eLMP_FadingOut = "eLMP_FadingOut"
    eLMP_Finished = "eLMP_Finished"
