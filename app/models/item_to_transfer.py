from dataclasses import dataclass

@dataclass
class ItemToTransfer:
    warehouse_item_id: int
    item_name: str
    quantity_available: float
    quantity_to_transfer: float
