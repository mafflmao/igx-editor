# EOptionsSaveVersion.py

from enum import Enum

class EOptionsSaveVersion(Enum):
    eOSV_INVALID = "eOSV_INVALID"
    eOSV_initialVersion = "eOSV_initialVersion"
    eOSV_AddedToyAccoladesToGlobalSave = "eOSV_AddedToyAccoladesToGlobalSave"
    eOSV_AllToyCollectiblesToGlobalSave = "eOSV_AllToyCollectiblesToGlobalSave"
    eOSV_GameStateToGlobalSave = "eOSV_GameStateToGlobalSave"
    eOSV_AddedLocksAndSkystonesToSave = "eOSV_AddedLocksAndSkystonesToSave"
    eOSV_SoulGemDropRate = "eOSV_SoulGemDropRate"
    eOSV_AddedPortalMasterStats = "eOSV_AddedPortalMasterStats"
    eOSV_AddedCollectibleTrackerGroupsAndMiscGameStates = "eOSV_AddedCollectibleTrackerGroupsAndMiscGameStates"
    eOSV_AnalyticsFunnelsAddedToGameState = "eOSV_AnalyticsFunnelsAddedToGameState"
    eOSV_AnalyticsElementalZoneEnteredAddedToGameState = "eOSV_AnalyticsElementalZoneEnteredAddedToGameState"
    eOSV_AnalyticsAddNewLeaderboard = "eOSV_AnalyticsAddNewLeaderboard"
    eOSV_AnalyticsAddTimePlayedWithHeroTracking = "eOSV_AnalyticsAddTimePlayedWithHeroTracking"
    eOSV_AnalyticsAddMoreLeaderboardTracking = "eOSV_AnalyticsAddMoreLeaderboardTracking"
    eOSV_AnalyticsAddGearbitsSpent = "eOSV_AnalyticsAddGearbitsSpent"
    eOSV_AnalyticsAddElementalGateAndDriverChallengeFunnels = "eOSV_AnalyticsAddElementalGateAndDriverChallengeFunnels"
    eOSV_AnalyticsMoreElementalGateAndDriverChallengeStats = "eOSV_AnalyticsMoreElementalGateAndDriverChallengeStats"
    eOSV_AddedLicenseAgreement = "eOSV_AddedLicenseAgreement"
    eOSV_AddedPurchaseAnalytics = "eOSV_AddedPurchaseAnalytics"
    eOSV_NEXT = "eOSV_NEXT"
