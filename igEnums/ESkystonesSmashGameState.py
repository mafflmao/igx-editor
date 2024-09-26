# ESkystonesSmashGameState.py

from enum import Enum

class ESkystonesSmashGameState(Enum):
    eSSGS_Dormant = "eSSGS_Dormant"
    eSSGS_Initialize = "eSSGS_Initialize"
    eSSGS_TutorialWaitToStart = "eSSGS_TutorialWaitToStart"
    eSSGS_TutorialStart = "eSSGS_TutorialStart"
    eSSGS_TutorialCombatStart = "eSSGS_TutorialCombatStart"
    eSSGS_TutorialAfterFirstResolve = "eSSGS_TutorialAfterFirstResolve"
    eSSGS_TutorialAfterSecondResolve = "eSSGS_TutorialAfterSecondResolve"
    eSSGS_TutorialResolveRound = "eSSGS_TutorialResolveRound"
    eSSGS_TutorialYourTurn = "eSSGS_TutorialYourTurn"
    eSSGS_TutorialChooseCard = "eSSGS_TutorialChooseCard"
    eSSGS_TutorialEndBeginning = "eSSGS_TutorialEndBeginning"
    eSSGS_TutorialEvents = "eSSGS_TutorialEvents"
    eSSGS_Mulligan = "eSSGS_Mulligan"
    eSSGS_NewRound = "eSSGS_NewRound"
    eSSGS_Turn = "eSSGS_Turn"
    eSSGS_WaitForTurn = "eSSGS_WaitForTurn"
    eSSGS_EndTurn = "eSSGS_EndTurn"
    eSSGS_ResolveRound = "eSSGS_ResolveRound"
    eSSGS_EndGame = "eSSGS_EndGame"
    eSSGS_NONE = "eSSGS_NONE"
