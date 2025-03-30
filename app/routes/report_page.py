from flask import Blueprint, render_template, request, send_file, flash
from io import BytesIO
import pandas as pd
from flask_login import login_required
from app.models import db, WarehouseInfo, WarehouseItems, EmpData, LoginEmp
from sqlalchemy import func

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/reports')
@login_required
def report_page():
    warehouse_info = WarehouseInfo.query.all()
    
    warehouse_data = db.session.query(
        WarehouseItems.warehouse_info_id,
        func.count(WarehouseItems.id).label("items_count"),
        func.sum(WarehouseItems.Item_Total_Cost).label("total_cost")
    ).group_by(WarehouseItems.warehouse_info_id).all()
    
    warehouse_names = {wi.Warehouse_Info_Id: wi.W_Name for wi in warehouse_info}
    
    context = {
        "warehouse_names": [warehouse_names.get(wd[0], "Unknown") for wd in warehouse_data],
        "warehouse_items_counts": [wd[1] for wd in warehouse_data],
        "warehouse_items_costs": [wd[2] for wd in warehouse_data],
        "warehouse_info": warehouse_info
    }
    
    return render_template("reports/report_page.html", **context)


def generate_excel(data, columns, sheet_name, filename):
    df = pd.DataFrame(data, columns=columns)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    output.seek(0)
    return send_file(output, download_name=filename, as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@report_bp.route('/reports/download/warehouse', methods=['GET'])
@login_required
def download_warehouse_report():
    data = db.session.query(
    WarehouseInfo.W_Name.label("Name"),
    WarehouseInfo.W_Location.label("Location"),
    WarehouseInfo.W_Pincode.label("PinCode"),
    WarehouseInfo.W_Total_capacity.label("Total Capacity"),
    WarehouseInfo.W_Space_Available.label("Space Available"),
    WarehouseInfo.W_Percent_Full.label("Percent Full"),
    func.count(WarehouseItems.id).label("Item Count"),
    func.sum(WarehouseItems.Item_Total_Cost).label("Total Cost of All Items")
).outerjoin(WarehouseItems, WarehouseItems.warehouse_info_id == WarehouseInfo.Warehouse_Info_Id) \
.group_by(
    WarehouseInfo.Warehouse_Info_Id, 
    WarehouseInfo.W_Name, 
    WarehouseInfo.W_Location, 
    WarehouseInfo.W_Pincode, 
    WarehouseInfo.W_Total_capacity, 
    WarehouseInfo.W_Space_Available, 
    WarehouseInfo.W_Percent_Full
).all()

    
    return generate_excel(data, [
        "Name", "Location", "PinCode", "Total Capacity", "Space Available", 
        "Percent Full", "Item Count", "Total Cost of All Items"
    ], 'Warehouse Report', "WarehouseReport_All.xlsx")


@report_bp.route('/reports/download/items', methods=['GET'])
@login_required
def download_items_report():
    warehouse_id = request.args.get('warehouseId', type=int)
    if not warehouse_id:
        flash("Please select a warehouse.", "warning")
        return "Please select a warehouse.", 400

    items = WarehouseItems.query.filter_by(warehouse_info_id=warehouse_id).all()
    
    data = [{
        "Item Name": item.Item_Name,
        "Quantity": item.Item_Unit_Quant,
        "Space per Unit": item.Item_Capacity_Quant,
        "Total Space Acquired": item.Item_Space_Acquired,
        "Cost Per Unit": item.Item_Price_Per_Unit,
        "Total Cost": item.Item_Total_Cost
    } for item in items]
    
    return generate_excel(data, [
        "Item Name", "Quantity", "Space per Unit", "Total Space Acquired", "Cost Per Unit", "Total Cost"
    ], 'Items Report', f"ItemsReport_Warehouse{warehouse_id}.xlsx")


@report_bp.route('/reports/download/managers', methods=['GET'])
@login_required
def download_managers_report():
    managers = db.session.query(
        LoginEmp.Name.label("Name"),
        LoginEmp.Email.label("Email"),
        LoginEmp.Role.label("Role"),
        LoginEmp.Username.label("Username"),
        WarehouseInfo.W_Name.label("Warehouse")
    ).join(WarehouseInfo, WarehouseInfo.Warehouse_Info_Id == LoginEmp.Warehouse_Info_Id)\
    .filter(LoginEmp.Role.contains("user")).all()
    
    return generate_excel(managers, ["Name", "Email", "Role", "Username", "Warehouse"], 'Managers Report', "ManagersReport.xlsx")


@report_bp.route('/reports/download/employees', methods=['GET'])
@login_required
def download_employee_report():
    warehouse_id = request.args.get('warehouseId', type=int)
    if not warehouse_id:
        flash("Please select a warehouse.", "warning")
        return "Please select a warehouse.", 400

    employees = db.session.query(
        EmpData.Name.label("Name"),
        EmpData.Email.label("Email"),
        EmpData.Phone.label("Phone"),
        EmpData.Address.label("Address"),
        EmpData.Pincode.label("PinCode"),
        WarehouseInfo.W_Name.label("Warehouse")
    ).join(WarehouseInfo, WarehouseInfo.Warehouse_Info_Id == EmpData.Warehouse_Info_Id)\
    .filter(EmpData.Warehouse_Info_Id == warehouse_id).all()
    
    return generate_excel(employees, ["Name", "Email", "Phone", "Address", "PinCode", "Warehouse"], 'Employees Report', f"EmployeesReport_Warehouse{warehouse_id}.xlsx")

@report_bp.route('/reports/download/page', methods=['GET'])
def download_page():
    return render_template("reports/download_page.html")