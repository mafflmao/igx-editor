# EPerformanceMonitorCounter.py

from enum import Enum

class EPerformanceMonitorCounter(Enum):
    ePMC_Frame = "ePMC_Frame"
    ePMC_Gui = "ePMC_Gui"
    ePMC_Game = "ePMC_Game"
    ePMC_VfxPreUpdate = "ePMC_VfxPreUpdate"
    ePMC_Logic = "ePMC_Logic"
    ePMC_EntityManagement = "ePMC_EntityManagement"
    ePMC_Havok = "ePMC_Havok"
    ePMC_AttachmentSystem = "ePMC_AttachmentSystem"
    ePMC_VfxPostUpdate = "ePMC_VfxPostUpdate"
    ePMC_Render = "ePMC_Render"
    ePMC_Audio = "ePMC_Audio"
    ePMC_ActorThink = "ePMC_ActorThink"
    ePMC_Script = "ePMC_Script"
    ePMC_Max = "ePMC_Max"
