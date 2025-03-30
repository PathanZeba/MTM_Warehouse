from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.decorators import superuser_required
import re
from app.models import WarehouseInfo, WarehouseItems
from app.forms.item_transfer_form import ItemTransferForm
from app.services import WarehouseService
from app.forms.warehouse_transfer_form import WarehouseTransferForm
from app.services import ListPageCountService
import traceback
from app.models. warehouse_info import WarehouseInfo
from sqlalchemy.exc import SQLAlchemyError



action_bp = Blueprint('action_bp', __name__,url_prefix='/MTM')
warehouse_service = WarehouseService()

@action_bp.route('/viewActions', methods=['GET'])
@login_required
def list_actions():
    w_count = WarehouseInfo.query.count()
    r_count = WarehouseItems.query.count()
    e_count = WarehouseItems.query.count()
    
    wre_count = wre_count = ListPageCountService(w_count, e_count, e_count)
    return render_template('action/list_actions.html', wre_count=wre_count, w_count=w_count)

#  Superuser-Only: Add Warehouse Page (GET)
@action_bp.route('/manage/addWareHouse', methods=['GET'])
@superuser_required
def add_warehouse_page():
    return render_template('action/add_warehouse.html', warehouse_info=WarehouseInfo())
#  Superuser-Only: Add Warehouse Info (POST)
@action_bp.route('/manage/addWareHouse', methods=['POST'])
@superuser_required
def add_warehouse_info():
    name = request.form.get('name', '').strip()
    location = request.form.get('location', '').strip()
    pincode = request.form.get('pincode', '').strip()
    capacity_value = request.form.get('capacity', '').strip()

    if not name:
        flash("Enter valid warehouse name", "danger")
        return redirect(url_for('action_bp.add_warehouse_page'))
    if not location:
        flash("Enter valid location", "danger")
        return redirect(url_for('action_bp.add_warehouse_page'))
    if not pincode:
        flash("Enter valid postal code", "danger")
        return redirect(url_for('action_bp.add_warehouse_page'))
    
    postal_code_pattern = r"^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$"
    if not re.match(postal_code_pattern, pincode.upper()):
        flash("Invalid postal code format. Use: 'N2M 5C7'", "danger")
        return redirect(url_for('action_bp.add_warehouse_page'))

    try:
        total_capacity = float(capacity_value)
    except ValueError:
        flash("Enter valid numeric total capacity", "danger")
        return redirect(url_for('action_bp.add_warehouse_page'))

    existing_warehouse = WarehouseInfo.query.filter_by(w_pincode=pincode).first()
    if existing_warehouse:
        flash("A warehouse with this postal code already exists!", "warning")
        return redirect(url_for('action_bp.add_warehouse_page'))

    warehouse_info = WarehouseInfo(
        W_Name=name,  
        W_Location=location,
        W_Pincode=pincode,
        W_Total_capacity=total_capacity,
        W_Space_Available=total_capacity,
        W_Percent_Full=0
    )

    db.session.add(warehouse_info)
    db.session.commit()

    flash("Warehouse added successfully!", "success")
    return redirect(url_for('action_bp.list_actions'))





    

@action_bp.route('/transferItems', methods=['GET', 'POST'])
@login_required
def transfer_items():
    form = WarehouseTransferForm()
    warehouses = WarehouseInfo.query.all()
    form.source_warehouse_id.choices = [(w.id, w.w_name) for w in warehouses]
    form.destination_warehouse_id.choices = [(w.id, w.w_name) for w in warehouses]
    
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('action_bp.confirm_transfer'))
    
    items = WarehouseItems.query.all()
    return render_template('action/transfer_items.html', form=form, items=items)

@action_bp.route('/confirmTransfer', methods=['POST'])
@login_required
def confirm_transfer():
    source_id = request.form.get('source_warehouse_id')
    destination_id = request.form.get('destination_warehouse_id')
    items_to_transfer = request.form.getlist('items')
    
    if len(items_to_transfer) > 1:
        for item_id in items_to_transfer:
            item = WarehouseItems.query.get(item_id)
            quantity = int(request.form.get(f'quantity_{item_id}', 0))
            
            if item and quantity > 0:
                item.item_unit_quant -= quantity
                existing_item = WarehouseItems.query.filter_by(
                    item_name=item.item_name, warehouse_info_id=destination_id
                ).first()
                
                if existing_item:
                    existing_item.item_unit_quant += quantity
                else:
                    new_item = WarehouseItems(
                        item_name=item.item_name,
                        item_capacity_quant=item.item_capacity_quant,
                        item_space_accuired=item.item_space_accuired,
                        item_price_per_unit=item.item_price_per_unit,
                        item_unit_quant=quantity,
                        warehouse_info_id=destination_id
                    )
                    db.session.add(new_item)
        db.session.commit()
    
    flash('Last action has been successfully fulfilled.', 'success')
    return redirect(url_for('action_bp.transfer_items'))

@action_bp.route('/get_items_for_warehouse')
@login_required
def get_items_for_warehouse():
    warehouse_id = request.args.get('warehouse_id', type=int)
    items = WarehouseItems.query.filter_by(warehouse_info_id=warehouse_id).all()
    
    items_data = [{
        'warehouse_item_id': item.warehouse_items_id,
        'item_name': item.item_name,
        'quantity_available': item.item_unit_quant or 0
    } for item in items]
    
    return jsonify(items_data)
