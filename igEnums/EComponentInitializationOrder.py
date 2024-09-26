# EComponentInitializationOrder.py

from enum import Enum

class EComponentInitializationOrder(Enum):
    eCIO_ProxyComponent = "eCIO_ProxyComponent"
    eCIO_ShapeshifterComponent = "eCIO_ShapeshifterComponent"
    eCIO_BehaviorComponent = "eCIO_BehaviorComponent"
    eCIO_PhysicsComponent = "eCIO_PhysicsComponent"
    eCIO_TriggerVolumeComponent = "eCIO_TriggerVolumeComponent"
    eCIO_NavMoverComponent = "eCIO_NavMoverComponent"
    eCIO_LinearVehicleSplineMoverComponent = "eCIO_LinearVehicleSplineMoverComponent"
    eCIO_ProjectileComponent = "eCIO_ProjectileComponent"
    eCIO_Default = "eCIO_Default"
    eCIO_DotNetComponent = "eCIO_DotNetComponent"
    eCIO_EntityGroupComponent = "eCIO_EntityGroupComponent"
