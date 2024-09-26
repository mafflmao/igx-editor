# ESpawnMessageType.py

from enum import Enum

class ESpawnMessageType(Enum):
    eSMT_ProjectileSpawn = "eSMT_ProjectileSpawn"
    eSMT_ProjectileSpawnWithReticle = "eSMT_ProjectileSpawnWithReticle"
    eSMT_ProjectileSpawnWithSpeed = "eSMT_ProjectileSpawnWithSpeed"
    eSMT_ProjectileSpawnWithSpeedReticle = "eSMT_ProjectileSpawnWithSpeedReticle"
    eSMT_ProjectileSpawnWithHoming = "eSMT_ProjectileSpawnWithHoming"
    eSMT_ProjectileSpawnWithAiming = "eSMT_ProjectileSpawnWithAiming"
