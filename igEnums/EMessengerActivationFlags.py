# EMessengerActivationFlags.py

from enum import Enum

class EMessengerActivationFlags(Enum):
    eMAF_None = "eMAF_None"
    eMAF_OnAct = "eMAF_OnAct"
    eMAF_OnDamage = "eMAF_OnDamage"
    eMAF_OnDeath = "eMAF_OnDeath"
    eMAF_OnEnter = "eMAF_OnEnter"
    eMAF_OnExit = "eMAF_OnExit"
    eMAF_OnRemove = "eMAF_OnRemove"
    eMAF_OnStart = "eMAF_OnStart"
    eMAF_OnTouch = "eMAF_OnTouch"
