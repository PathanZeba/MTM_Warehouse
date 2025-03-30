from app.models import WarehouseInfo, WarehouseItems
from abc import ABC, abstractmethod

class IWarehouseService(ABC):

    @abstractmethod
    def warehouse_space_available(self, warehouse_info: WarehouseInfo, space_occupied_by_item: float) -> WarehouseInfo:
        pass

    @abstractmethod
    def warehouse_percent_full(self, warehouse_info: WarehouseInfo) -> WarehouseInfo:
        pass

    @abstractmethod
    def w_percentage(self, warehouse_info: WarehouseInfo) -> float:
        pass

    @abstractmethod
    def w_space_available(self, warehouse_info: WarehouseInfo) -> float:
        pass

    @abstractmethod
    def total_price(self, warehouse_items: WarehouseItems) -> WarehouseItems:
        pass


# ✅ **Concrete Implementation**
class WarehouseService(IWarehouseService):

    def warehouse_space_available(self, warehouse_info: WarehouseInfo, space_occupied_by_item: float) -> WarehouseInfo:
        warehouse_info.W_SpaceAvailable -= space_occupied_by_item
        return warehouse_info

    def warehouse_percent_full(self, warehouse_info: WarehouseInfo) -> WarehouseInfo:
        warehouse_info.W_PercentFull = ((warehouse_info.W_TotalSpace - warehouse_info.W_SpaceAvailable) / warehouse_info.W_TotalSpace) * 100
        return warehouse_info

    def w_percentage(self, warehouse_info: WarehouseInfo) -> float:
        return warehouse_info.W_PercentFull

    def w_space_available(self, warehouse_info: WarehouseInfo) -> float:
        return warehouse_info.W_SpaceAvailable

    def total_price(self, warehouse_items: WarehouseItems) -> WarehouseItems:
        warehouse_items.TotalPrice = warehouse_items.Item_Capacity_Quant * warehouse_items.Item_Unit_Quant
        return warehouse_items
