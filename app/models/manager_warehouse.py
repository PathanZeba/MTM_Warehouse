from typing import Optional
from dataclasses import dataclass
from .warehouse_info import WarehouseInfo
from .login_emp import LoginEmp

@dataclass
class ManagerWarehouseModel:
    warehouseInfo: Optional[WarehouseInfo] = None
    loginEmp: Optional[LoginEmp] = None
