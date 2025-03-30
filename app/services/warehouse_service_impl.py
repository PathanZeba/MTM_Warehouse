from app.models import WarehouseInfo, WarehouseItems
from app.services.warehouse_service import IWarehouseService

class WarehouseService(IWarehouseService):

    def warehouse_percent_full(self, warehouse_info: WarehouseInfo) -> WarehouseInfo:
        """Warehouse ka percentage full calculate aur update karega."""
        if warehouse_info.w_total_capacity == 0:  # ⚠️ ZeroDivisionError se bachne ke liye
            warehouse_info.w_percent_full = 100.0  # Full maana jayega
        else:
            percentage_full = (warehouse_info.w_space_available / warehouse_info.w_total_capacity) * 100
            warehouse_info.w_percent_full = round(100 - percentage_full, 2)

        return warehouse_info

    def warehouse_space_available(self, warehouse_info: WarehouseInfo, space_occupied_by_item: float) -> WarehouseInfo:
        """Warehouse me available space calculate aur update karega."""
        warehouse_info.w_space_available = max(0, warehouse_info.w_total_capacity - space_occupied_by_item)
        return warehouse_info

    def total_price(self, warehouse_item: WarehouseItems) -> WarehouseItems:
        """Warehouse item ka total price calculate karega."""
        warehouse_item.Item_total_cost = warehouse_item.Item_price_per_unit * warehouse_item.Item_Unit_Quant
        return warehouse_item

    def w_percentage(self, warehouse_info: WarehouseInfo) -> float:
        """Warehouse occupancy percentage return karega."""
        return warehouse_info.w_percent_full

    def w_space_available(self, warehouse_info: WarehouseInfo) -> float:
        """Warehouse me available space return karega."""
        return warehouse_info.w_space_available
