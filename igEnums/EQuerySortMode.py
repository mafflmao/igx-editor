# EQuerySortMode.py

from enum import Enum

class EQuerySortMode(Enum):
    eQSM_NoSort = "eQSM_NoSort"
    eQSM_SortByDistance = "eQSM_SortByDistance"
    eQSM_SortByFaceAngle = "eQSM_SortByFaceAngle"
    eQSM_SortByHealth = "eQSM_SortByHealth"
    eQSM_SortByLeftToRight = "eQSM_SortByLeftToRight"