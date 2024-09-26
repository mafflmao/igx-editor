# EDriverChallengeFunnel.py

from enum import Enum

class EDriverChallengeFunnel(Enum):
    eDCF_AtAcademy = "eDCF_AtAcademy"
    eDCF_NpcIntroComplete = "eDCF_NpcIntroComplete"
    eDCF_EligibleToStartChallenge = "eDCF_EligibleToStartChallenge"
    eDCF_ChallengeStarted = "eDCF_ChallengeStarted"
    eDCF_ChallengeCompleted = "eDCF_ChallengeCompleted"
