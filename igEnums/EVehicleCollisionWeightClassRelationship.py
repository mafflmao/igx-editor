# EVehicleCollisionWeightClassRelationship.py

from enum import Enum

class EVehicleCollisionWeightClassRelationship(Enum):
    eVCWCR_Equal = "eVCWCR_Equal"
    eVCWCR_SourceHigher = "eVCWCR_SourceHigher"
    eVCWCR_TargetHigher = "eVCWCR_TargetHigher"
    eVCWCR_All = "eVCWCR_All"
