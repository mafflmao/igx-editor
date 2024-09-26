# EStoryScrollState.py

from enum import Enum

class EStoryScrollState(Enum):
    eSSS_Initialize = "eSSS_Initialize"
    eSSS_HideTextChunk = "eSSS_HideTextChunk"
    eSSS_ShowFirstTextChunk = "eSSS_ShowFirstTextChunk"
    eSSS_ShowTextChunk = "eSSS_ShowTextChunk"
    eSSS_Shutdown = "eSSS_Shutdown"
