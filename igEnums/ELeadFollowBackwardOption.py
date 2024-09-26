# ELeadFollowBackwardOption.py

from enum import Enum

class ELeadFollowBackwardOption(Enum):
    eLFBO_None = "eLFBO_None"
    eLFBO_UseForwardAsBackwardMessage = "eLFBO_UseForwardAsBackwardMessage"
    eLFBO_UsePreviousTriggerForwardMessage = "eLFBO_UsePreviousTriggerForwardMessage"
