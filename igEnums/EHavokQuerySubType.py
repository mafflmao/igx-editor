# EHavokQuerySubType.py

from enum import Enum

class EHavokQuerySubType(Enum):
    eHQST_Invalid = "eHQST_Invalid"
    eHQST_StartWorld = "eHQST_StartWorld"
    eHQST_WorldPointCast = "eHQST_WorldPointCast"
    eHQST_WorldShapeCast = "eHQST_WorldShapeCast"
    eHQST_WorldPointClosestPoints = "eHQST_WorldPointClosestPoints"
    eHQST_WorldShapeClosestPoints = "eHQST_WorldShapeClosestPoints"
    eHQST_StartPair = "eHQST_StartPair"
    eHQST_PairPointCast = "eHQST_PairPointCast"
    eHQST_PairShapeCast = "eHQST_PairShapeCast"
    eHQST_PairPointClosestPoints = "eHQST_PairPointClosestPoints"
    eHQST_PairShapeClosestPoints = "eHQST_PairShapeClosestPoints"
    eHQST_Count = "eHQST_Count"
