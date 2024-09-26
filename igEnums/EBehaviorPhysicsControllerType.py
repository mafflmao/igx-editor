# EBehaviorPhysicsControllerType.py

from enum import Enum

class EBehaviorPhysicsControllerType(Enum):
    eBPCT_None = "eBPCT_None"
    eBPCT_CharacterRigidBody = "eBPCT_CharacterRigidBody"
    eBPCT_CharacterProxy = "eBPCT_CharacterProxy"
    eBPCT_SeaPack = "eBPCT_SeaPack"
    eBPCT_SkyPack = "eBPCT_SkyPack"
