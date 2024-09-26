# ELinkUsageFlag.py

from enum import Enum

class ELinkUsageFlag(Enum):
    eLUF_LowJump = "eLUF_LowJump"
    eLUF_HighJump = "eLUF_HighJump"
    eLUF_DropOff = "eLUF_DropOff"
    eLUF_Gap = "eLUF_Gap"
    eLUF_Breadcrumbs = "eLUF_Breadcrumbs"
