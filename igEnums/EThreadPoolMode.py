# EThreadPoolMode.py

from enum import Enum

class EThreadPoolMode(Enum):
    eTPM_Idle = "eTPM_Idle"
    eTPM_HavokStep = "eTPM_HavokStep"
    eTPM_JobQueue = "eTPM_JobQueue"
    eTPM_TaskQueue = "eTPM_TaskQueue"
