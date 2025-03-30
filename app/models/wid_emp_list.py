from typing import List, Optional
from dataclasses import dataclass
from .emp_data import EmpData  # Ensure correct import path

@dataclass
class WIDEmpListModel:
    W_ID: int
    empDatas: Optional[List[EmpData]] = None
