# EMobileShadowState.py

from enum import Enum

class EMobileShadowState(Enum):
    eMSS_LetGameDecide = "eMSS_LetGameDecide"
    eMSS_CastsShadows = "eMSS_CastsShadows"
    eMSS_RecievesShadows = "eMSS_RecievesShadows"
    eMSS_DoesNotCastOrReceiveShadows = "eMSS_DoesNotCastOrReceiveShadows"
