from dataclasses import dataclass
from sqlalchemy.orm import Session
from models.warehouse_info import WarehouseInfo
from models.login_emp import LoginEmp
from models.emp_data import EmpData

@dataclass
class ListActionService:
    db: Session

    def warehouse_count(self) -> int:
        return self.db.query(WarehouseInfo).count()

    def login_emp_count(self) -> int:
        return self.db.query(LoginEmp).count()

    def emp_data_count(self) -> int:
        return self.db.query(EmpData).count()

    @property
    def all_warehouse_count(self) -> int:
        return self.warehouse_count() or 0

    @property
    def all_login_emp_count(self) -> int:
        return self.login_emp_count() or 0

    @property
    def all_emp_data_count(self) -> int:
        return self.emp_data_count() or 0
