from dataclasses import dataclass, field
from typing import List, Optional
from .warehouse_info import WarehouseInfo
from .item_to_transfer import ItemToTransfer

@dataclass
class ItemTransferViewModel:
    source_warehouse_id: Optional[int] = None
    destination_warehouse_id: Optional[int] = None
    warehouses: List[WarehouseInfo] = field(default_factory=list)
    items_to_transfer: List[ItemToTransfer] = field(default_factory=list)
