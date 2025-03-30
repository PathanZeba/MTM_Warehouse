from typing import Optional, List
from dataclasses import dataclass
from .warehouse_info import WarehouseInfo

@dataclass
class DownloadReportViewModel:
    selected_warehouse_id: Optional[int] = None
    warehouse_info: List[WarehouseInfo] = None
