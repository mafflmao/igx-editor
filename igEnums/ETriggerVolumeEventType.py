# ETriggerVolumeEventType.py

from enum import Enum

class ETriggerVolumeEventType(Enum):
    eTVET_None = "eTVET_None"
    eTVET_Enter = "eTVET_Enter"
    eTVET_Exit = "eTVET_Exit"
    eTVET_Touch = "eTVET_Touch"
    eTVET_Act = "eTVET_Act"
    eTVET_DeAct = "eTVET_DeAct"
    eTVET_SendEntityEvent = "eTVET_SendEntityEvent"
    eTVET_NetworkEnabled = "eTVET_NetworkEnabled"
