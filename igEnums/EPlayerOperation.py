# EPlayerOperation.py

from enum import Enum

class EPlayerOperation(Enum):
    ePO_Added = "ePO_Added"
    ePO_Removed = "ePO_Removed"
    ePO_ChangedHero = "ePO_ChangedHero"
    ePO_ChangedChannel = "ePO_ChangedChannel"
