from dataclasses import dataclass
from typing import Optional
from models.warehouse_info import WarehouseInfo
from models.emp_data import EmpData

@dataclass
class EmployeeWarehouseModel:
    warehouse_info: Optional[WarehouseInfo] = None
    emp_data: Optional[EmpData] = None
