# EVehicleDockingState.py

from enum import Enum

class EVehicleDockingState(Enum):
    eVDS_Inactive = "eVDS_Inactive"
    eVDS_AwaitingPlayer = "eVDS_AwaitingPlayer"
    eVDS_TransitionQueued = "eVDS_TransitionQueued"
    eVDS_VerifyingVehicleType = "eVDS_VerifyingVehicleType"
    eVDS_DriverEnterSequence = "eVDS_DriverEnterSequence"
    eVDS_WaitingForPlayersToDock = "eVDS_WaitingForPlayersToDock"
    eVDS_WaitingForPlayersToExitAndDock = "eVDS_WaitingForPlayersToExitAndDock"
    eVDS_VehicleChangingFormParked = "eVDS_VehicleChangingFormParked"
    eVDS_VehicleChangingFormDriving = "eVDS_VehicleChangingFormDriving"
    eVDS_VehicleChangingFormInvisible = "eVDS_VehicleChangingFormInvisible"
    eVDS_VehicleDocked = "eVDS_VehicleDocked"
    eVDS_VehicleDockedWaitingForRemoteTransition = "eVDS_VehicleDockedWaitingForRemoteTransition"
    eVDS_TransitionCooldown = "eVDS_TransitionCooldown"
    eVDS_VehicleDocking = "eVDS_VehicleDocking"
    eVDS_VehicleDockingEnd = "eVDS_VehicleDockingEnd"
    eVDS_DriverExitSequence = "eVDS_DriverExitSequence"
