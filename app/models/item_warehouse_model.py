from dataclasses import dataclass
from .warehouse_items import WarehouseItems
from .warehouse_info import WarehouseInfo

@dataclass
class ItemWarehouseModel:
    warehouse_items: WarehouseItems
    warehouse_info: WarehouseInfo
