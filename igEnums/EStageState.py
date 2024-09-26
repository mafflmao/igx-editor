# EStageState.py

from enum import Enum

class EStageState(Enum):
    eSS_Invalid = "eSS_Invalid"
    eSS_Unprepared = "eSS_Unprepared"
    eSS_Preparing = "eSS_Preparing"
    eSS_Waiting = "eSS_Waiting"
    eSS_Playing = "eSS_Playing"
    eSS_PlayingMovie = "eSS_PlayingMovie"
    eSS_Finished = "eSS_Finished"
