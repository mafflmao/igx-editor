# ESyncFlag.py

from enum import Enum

class ESyncFlag(Enum):
    eSF_MagicMomentEnter = "eSF_MagicMomentEnter"
    eSF_MagicMomentExit = "eSF_MagicMomentExit"
    eSF_MagicMomentExitConfirm = "eSF_MagicMomentExitConfirm"
    eSF_MagicMomentEnabled = "eSF_MagicMomentEnabled"
    eSF_MagicMomentHeroAndVehicleActorsReady = "eSF_MagicMomentHeroAndVehicleActorsReady"
    eSF_MagicMomentError = "eSF_MagicMomentError"
    eSF_SkipSyncPause = "eSF_SkipSyncPause"
    eSF_LevelResultsActive = "eSF_LevelResultsActive"
    eSF_LevelResultsReadyToExit = "eSF_LevelResultsReadyToExit"
    eSF_LevelResultsExited = "eSF_LevelResultsExited"
    eSF_ReadyToEnterRace = "eSF_ReadyToEnterRace"
    eSF_Type1 = "eSF_Type1"
    eSF_Type2 = "eSF_Type2"
    eSF_FadeOut = "eSF_FadeOut"
