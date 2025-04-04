from typing import List, Optional
from dataclasses import dataclass
from .warehouse_items import WarehouseItems  

@dataclass
class WIDItemListModel:
    W_ID: int
    warehouseItems: Optional[List[WarehouseItems]] = None
