# EAnimationUpdateStage.py

from enum import Enum

class EAnimationUpdateStage(Enum):
    eAUS_EarlyUpdate = "eAUS_EarlyUpdate"
    eAUS_PhysicsOnly = "eAUS_PhysicsOnly"
    eAUS_WithHavok = "eAUS_WithHavok"
    eAUS_Idle = "eAUS_Idle"
