# CriticalType.py

from enum import Enum

class CriticalType(Enum):
    kCriticalNone = "kCriticalNone"
    kCriticalStart = "kCriticalStart"
    kCriticalEnd = "kCriticalEnd"
    kCriticalOnInterrupt = "kCriticalOnInterrupt"