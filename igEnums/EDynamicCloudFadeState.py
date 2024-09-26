# EDynamicCloudFadeState.py

from enum import Enum

class EDynamicCloudFadeState(Enum):
    eDCFS_Normal = "eDCFS_Normal"
    eDCFS_FadingOut = "eDCFS_FadingOut"
    eDCFS_FadedOut = "eDCFS_FadedOut"
    eDCFS_FadingIn = "eDCFS_FadingIn"
