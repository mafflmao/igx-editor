# ENetworkReplicaType.py

from enum import Enum

class ENetworkReplicaType(Enum):
    eNRT_FromMeta = "eNRT_FromMeta"
    eNRT_Entity = "eNRT_Entity"
    eNRT_EntityVolumeCull = "eNRT_EntityVolumeCull"
    eNRT_Hero = "eNRT_Hero"
    eNRT_Vehicle = "eNRT_Vehicle"
    eNRT_HealthObject = "eNRT_HealthObject"
    eNRT_Statistic = "eNRT_Statistic"
    eNRT_Event = "eNRT_Event"
    eNRT_VehicleCustomization = "eNRT_VehicleCustomization"
    eNRT_Slider = "eNRT_Slider"
    eNRT_LoadSync = "eNRT_LoadSync"
