from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_principal import Permission, RoleNeed
from app import db
from app.models.user import User
from app.models.warehouse_info import WarehouseInfo
from app.models.login_emp import LoginEmp
from app.models.emp_data import EmpData
from app.models.warehouse_items import WarehouseItems
from app.services.warehouse_service import WarehouseService


warehouse_bp = Blueprint('warehouse', __name__, url_prefix='/warehouse')


super_user_permission = Permission(RoleNeed('superuser'))
master_user_permission = Permission(RoleNeed('masteruser'))


warehouse_service = WarehouseService()


@warehouse_bp.route('/view/<int:id>')
@login_required
def open_warehouse(id):
    warehouse_info = WarehouseInfo.query.get(id)
    if not warehouse_info:
        flash("Warehouse not found!", "danger")
        return redirect(url_for("warehouse.open_warehouse", id=current_user.warehouse_id))  

    login_emp = LoginEmp.query.filter_by(warehouse_info_id=id).all()
    emp_data = EmpData.query.filter_by(warehouse_info_id=id).all()
    all_items = WarehouseItems.query.filter_by(warehouse_info_id=id).all()

    total = sum(item.item_space_acquired for item in all_items)
    warehouse_info = warehouse_service.warehouse_space_available(warehouse_info, total)
    warehouse_info = warehouse_service.warehouse_percent_full(warehouse_info)

    db.session.commit()

    return render_template('warehouse/warehouse.html', warehouse_info=warehouse_info, login_emp=login_emp, emp_data=emp_data, all_items=all_items)


@warehouse_bp.route('/<int:id>/managers', methods=['GET'])
@login_required
def view_managers(id):
    if not super_user_permission.can():
        flash("You do not have permission to view managers.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=id))

    warehouse_info = WarehouseInfo.query.get_or_404(id)
    managers = LoginEmp.query.filter_by(warehouse_info_id=id).all()
    return render_template('warehouse/managers.html', warehouse_info=warehouse_info, managers=managers)

@warehouse_bp.route('/addmanager', methods=['POST'])
@login_required
def add_manager():
    if not super_user_permission.can():
        flash("You do not have permission to add a manager.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=current_user.warehouse_id))

    warehouse_id = request.form.get('warehouse_info')
    name = request.form.get('name')
    username = request.form.get('username')

    if warehouse_id and name and username:
        login_emp = LoginEmp(name=name, username=username, warehouse_info_id=warehouse_id)
        db.session.add(login_emp)
        db.session.commit()
        flash(f'Manager "{name}" added successfully.', 'success')
        return redirect(url_for('warehouse.view_managers', id=warehouse_id))

    flash('Error adding manager.', 'danger')
    return redirect(url_for('warehouse.view_managers', id=warehouse_id))


@warehouse_bp.route('/<int:id>/employees', methods=['GET'])
@login_required
def view_employees(id):
    if not master_user_permission.can():
        flash("You do not have permission to view employees.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=id))

    warehouse_info = WarehouseInfo.query.get_or_404(id)
    employees = EmpData.query.filter_by(warehouse_info_id=id).all()
    return render_template('warehouse/employee.html', warehouse_info=warehouse_info, employees=employees)

@warehouse_bp.route('/addemployee', methods=['POST'])
@login_required
def add_employee():
    if not master_user_permission.can():
        flash("You do not have permission to add an employee.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=current_user.warehouse_id))

    warehouse_id = request.form.get('warehouse_info')
    name = request.form.get('name')

    if warehouse_id and name:
        employee = EmpData(name=name, warehouse_info_id=warehouse_id)
        db.session.add(employee)
        db.session.commit()
        flash(f'Employee "{name}" added successfully.', 'success')
        return redirect(url_for('warehouse.view_employees', id=warehouse_id))

    flash('Error adding employee.', 'danger')
    return redirect(url_for('warehouse.view_employees', id=warehouse_id))


@warehouse_bp.route('/<int:id>/items', methods=['GET'])
@login_required
def view_items(id):
    if not master_user_permission.can():
        flash("You do not have permission to view items.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=id))

    warehouse_info = WarehouseInfo.query.get_or_404(id)
    items = WarehouseItems.query.filter_by(warehouse_info_id=id).all()
    return render_template('warehouse/items.html', warehouse_info=warehouse_info, items=items)

@warehouse_bp.route('/additem', methods=['POST'])
@login_required
def add_item():
    if not master_user_permission.can():
        flash("You do not have permission to add an item.", "danger")
        return redirect(url_for('warehouse.open_warehouse', id=current_user.warehouse_id))

    warehouse_id = request.form.get('warehouse_info')
    item_name = request.form.get('item_name')
    item_capacity_quant = request.form.get('item_capacity_quant')
    item_unit_quant = request.form.get('item_unit_quant')

    try:
        item_capacity_quant = float(item_capacity_quant)
        item_unit_quant = float(item_unit_quant)
    except ValueError:
        flash("Invalid input for item quantity.", "danger")
        return redirect(url_for('warehouse.view_items', id=warehouse_id))

    warehouse_info = WarehouseInfo.query.get_or_404(warehouse_id)
    total_space_required = item_capacity_quant * item_unit_quant

    if warehouse_info.W_SpaceAvailable < total_space_required:
        flash('Not enough space in the warehouse.', 'danger')
        return redirect(url_for('warehouse.view_items', id=warehouse_id))

    existing_item = WarehouseItems.query.filter_by(Item_Name=item_name, warehouse_info_id=warehouse_id).first()
    if existing_item:
        flash('Item already exists.', 'danger')
        return redirect(url_for('warehouse.view_items', id=warehouse_id))

    new_item = WarehouseItems(
        Item_Name=item_name,
        Item_Capacity_Quant=item_capacity_quant,
        Item_Unit_Quant=item_unit_quant,
        warehouse_info_id=warehouse_id,
        Item_SpaceAccuired=total_space_required  
    )

    db.session.add(new_item)
    db.session.commit()
    flash(f'Item "{item_name}" added successfully.', 'success')
    return redirect(url_for('warehouse.view_items', id=warehouse_id))
