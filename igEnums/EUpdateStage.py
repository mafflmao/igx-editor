# EUpdateStage.py

from enum import Enum

class EUpdateStage(Enum):
    eUS_preUpdate = "eUS_preUpdate"
    eUS_preUpdateRenderContext = "eUS_preUpdateRenderContext"
    eUS_mainUpdate = "eUS_mainUpdate"
    eUS_postUpdate = "eUS_postUpdate"
    eUS_submit = "eUS_submit"
    eUS_initial = "eUS_initial"
