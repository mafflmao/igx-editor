# EGuiMenuSoundEvent.py

from enum import Enum

class EGuiMenuSoundEvent(Enum):
    eGMSE_None = "eGMSE_None"
    eGMSE_ProjectLoad = "eGMSE_ProjectLoad"
    eGMSE_ProjectUnload = "eGMSE_ProjectUnload"
    eGMSE_ProjectInput = "eGMSE_ProjectInput"
    eGMSE_PlaceableInput = "eGMSE_PlaceableInput"
    eGMSE_ProjectFocus = "eGMSE_ProjectFocus"
    eGMSE_PlaceableFocus = "eGMSE_PlaceableFocus"
