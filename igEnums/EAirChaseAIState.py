# EAirChaseAIState.py

from enum import Enum

class EAirChaseAIState(Enum):
    eACAIS_Inactive = "eACAIS_Inactive"
    eACAIS_Intro = "eACAIS_Intro"
    eACAIS_Pursuit = "eACAIS_Pursuit"
    eACAIS_Attack = "eACAIS_Attack"
    eACAIS_Outro = "eACAIS_Outro"
