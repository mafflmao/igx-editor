# ECRMMessageAction.py

from enum import Enum

class ECRMMessageAction(Enum):
    eCRMMA_Invalid = "eCRMMA_Invalid"
    eCRMMA_Popup = "eCRMMA_Popup"
    eCRMMA_Goto = "eCRMMA_Goto"
    eCRMMA_Video = "eCRMMA_Video"
    eCRMMA_AwardKit = "eCRMMA_AwardKit"
    eCRMMA_Count = "eCRMMA_Count"
