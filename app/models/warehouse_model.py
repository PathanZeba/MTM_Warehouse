from models.warehouse_info import WarehouseInfo
from models.login_emp import LoginEmp
from models.emp_data import EmpData
from models.warehouse_items import WarehouseItems

class WarehouseModel:
    """
    WarehouseModel ek wrapper class hai jo WarehouseInfo, LoginEmp, EmpData, 
    aur WarehouseItems models ko encapsulate karti hai.
    """
    def __init__(self, warehouse_info=None, login_emps=None, emp_data=None, all_items=None):
        self.warehouse_info = warehouse_info  # WarehouseInfo instance
        self.login_emps = login_emps if login_emps else []  # List of LoginEmp instances
        self.emp_data = emp_data if emp_data else []  # List of EmpData instances
        self.all_items = all_items if all_items else []  # List of WarehouseItems instances

    def __repr__(self):
        return f"<WarehouseModel(Warehouse: {self.warehouse_info}, Employees: {len(self.login_emps)}, Items: {len(self.all_items)})>"
