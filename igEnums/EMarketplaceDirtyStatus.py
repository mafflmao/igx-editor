# EMarketplaceDirtyStatus.py

from enum import Enum

class EMarketplaceDirtyStatus(Enum):
    eMDS_None = "eMDS_None"
    eMDS_InventoryChanged = "eMDS_InventoryChanged"
    eMDS_BalancesChanged = "eMDS_BalancesChanged"
    eMDS_StoreProductsChanged = "eMDS_StoreProductsChanged"
    eMDS_StorePurchasesChanged = "eMDS_StorePurchasesChanged"
    eMDS_AllChanged = "eMDS_AllChanged"
