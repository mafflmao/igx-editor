# ECaptureSequenceStates.py

from enum import Enum

class ECaptureSequenceStates(Enum):
    eCSS_TransitionIn = "eCSS_TransitionIn"
    eCSS_Intro = "eCSS_Intro"
    eCSS_TrophySpawn = "eCSS_TrophySpawn"
    eCSS_TrophySpit = "eCSS_TrophySpit"
    eCSS_ScrollSpawn = "eCSS_ScrollSpawn"
    eCSS_ScrollIdle = "eCSS_ScrollIdle"
    eCSS_ScrollOut = "eCSS_ScrollOut"
    eCSS_Outro = "eCSS_Outro"
    eCSS_TransitionOut = "eCSS_TransitionOut"
    eCSS_None = "eCSS_None"
