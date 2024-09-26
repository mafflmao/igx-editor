# ECardState.py

from enum import Enum

class ECardState(Enum):
    eCS_FaceDownDown = "eCS_FaceDownDown"
    eCS_FaceDownUp = "eCS_FaceDownUp"
    eCS_FlippingDown = "eCS_FlippingDown"
    eCS_FlippingUp = "eCS_FlippingUp"
    eCS_FaceUpUp = "eCS_FaceUpUp"
    eCS_FaceUpDown = "eCS_FaceUpDown"
    eCS_AttackingCard = "eCS_AttackingCard"
    eCS_AttackingPlayer = "eCS_AttackingPlayer"
