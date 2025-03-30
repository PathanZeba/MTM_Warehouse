from typing import List, Optional
from dataclasses import dataclass
from .warehouse_info import WarehouseInfo
from .warehouse_items import WarehouseItems
from .emp_data import EmpData
from .login_emp import LoginEmp

@dataclass
class ReportViewModel:
    warehouseInfo: Optional[List[WarehouseInfo]] = None
    warehouseItems: Optional[List[WarehouseItems]] = None
    empDatas: Optional[List[EmpData]] = None
    loginEmps: Optional[List[LoginEmp]] = None

    w_Id: Optional[int] = None
    i_Id: Optional[int] = None
    m_Id: Optional[int] = None
    e_Id: Optional[int] = None
