# EMobileShadowStateOverride.py

from enum import Enum

class EMobileShadowStateOverride(Enum):
    eMSSO_Archetype = "eMSSO_Archetype"
    eMSSO_CastsShadows = "eMSSO_CastsShadows"
    eMSSO_ReceivesShadows = "eMSSO_ReceivesShadows"
    eMSSO_DoesNotCastOrReceiveShadows = "eMSSO_DoesNotCastOrReceiveShadows"
