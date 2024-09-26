# ETelegramTargetFlags.py

from enum import Enum

class ETelegramTargetFlags(Enum):
    eTTF_None = "eTTF_None"
    eTTF_SendMessageToSelf = "eTTF_SendMessageToSelf"
    eTTF_SendMessageToActivator = "eTTF_SendMessageToActivator"
    eTTF_SendMessageToWorldEntity = "eTTF_SendMessageToWorldEntity"
    eTTF_SendMessageToPlayers = "eTTF_SendMessageToPlayers"
    eTTF_SendMessageToClosestPlayer = "eTTF_SendMessageToClosestPlayer"
    eTTF_SendMessageToFarthestPlayer = "eTTF_SendMessageToFarthestPlayer"
    eTTF_SendMessageToParent = "eTTF_SendMessageToParent"
    eTTF_SendMessageToVehicle = "eTTF_SendMessageToVehicle"
