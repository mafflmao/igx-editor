# EPauseMenuState.py

from enum import Enum

class EPauseMenuState(Enum):
    ePMS_Normal = "ePMS_Normal"
    ePMS_FadingOut = "ePMS_FadingOut"
    ePMS_FadedOut = "ePMS_FadedOut"
    ePMS_AnimatingToFullscreen = "ePMS_AnimatingToFullscreen"
    ePMS_Fullscreen = "ePMS_Fullscreen"
    ePMS_Closing = "ePMS_Closing"
