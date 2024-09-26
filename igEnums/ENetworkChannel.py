# ENetworkChannel.py

from enum import Enum

class ENetworkChannel(Enum):
    eNC_Global = "eNC_Global"
    eNC_GameProgression = "eNC_GameProgression"
    eNC_StoryProgression = "eNC_StoryProgression"
    eNC_PortalTags = "eNC_PortalTags"
    eNC_VehiclePortalTags = "eNC_VehiclePortalTags"
    eNC_Level = "eNC_Level"
    eNC_HeroBegin = "eNC_HeroBegin"
    eNC_HeroEnd = "eNC_HeroEnd"
    eNC_VehicleBegin = "eNC_VehicleBegin"
    eNC_VehicleEnd = "eNC_VehicleEnd"
