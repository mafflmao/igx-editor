# EProjectileDeathReason.py

from enum import Enum

class EProjectileDeathReason(Enum):
    ePDR_Unknown = "ePDR_Unknown"
    ePDR_Timeout = "ePDR_Timeout"
    ePDR_Contact = "ePDR_Contact"
    ePDR_Damage = "ePDR_Damage"
