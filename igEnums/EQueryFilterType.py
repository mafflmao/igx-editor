# EQueryFilterType.py

from enum import Enum

class EQueryFilterType(Enum):
    EQFT_OnlyKeepResultsInQuery = "EQFT_OnlyKeepResultsInQuery"
    EQFT_RemoveResultsFromQuery = "EQFT_RemoveResultsFromQuery"