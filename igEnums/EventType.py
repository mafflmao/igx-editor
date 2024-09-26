# EventType.py

from enum import Enum

class EventType(Enum):
    eT_CombatIntro = "eT_CombatIntro"
    eT_AfterFirstResolve = "eT_AfterFirstResolve"
    eT_AfterSecondResolve = "eT_AfterSecondResolve"
    eT_PlayersFirstTurn = "eT_PlayersFirstTurn"
    eT_PlayerChooseCard = "eT_PlayerChooseCard"
    eT_AfterPlayerPlaysCard = "eT_AfterPlayerPlaysCard"
    eT_PlayerDamagesOpponent = "eT_PlayerDamagesOpponent"
    eT_OpponentDamagesPlayer = "eT_OpponentDamagesPlayer"
    eT_Overdrive = "eT_Overdrive"
    eT_ElementBuff = "eT_ElementBuff"
