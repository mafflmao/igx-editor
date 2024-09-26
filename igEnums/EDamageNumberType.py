# EDamageNumberType.py

from enum import Enum

class EDamageNumberType(Enum):
    eDNT_Health = "eDNT_Health"
    eDNT_Damage = "eDNT_Damage"
    eDNT_CriticalDamage = "eDNT_CriticalDamage"
    eDNT_Money = "eDNT_Money"
    eDNT_StatBoost = "eDNT_StatBoost"
    eDNT_SuperchargeDamage = "eDNT_SuperchargeDamage"
    eDNT_SuperchargeDamageCritical = "eDNT_SuperchargeDamageCritical"
    eDNT_Custom = "eDNT_Custom"
    eDNT_CustomSigned = "eDNT_CustomSigned"
