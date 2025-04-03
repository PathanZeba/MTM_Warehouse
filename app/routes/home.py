from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from app.models import user
from app.models.warehouse_info import WarehouseInfo
from app import db

#  Blueprint correctly defined
home_bp = Blueprint("home_bp", __name__, url_prefix="/home")

@home_bp.route('/')
@login_required  # Ensures user is logged in
def home_page():
    warehouse_infos = WarehouseInfo.query.all()
    
    if len(warehouse_infos) == 0:
        warehouse_infos.append(WarehouseInfo(Warehouse_Info_Id=-1))

    
    warehouse_dicts = [{col.name: getattr(w, col.name) for col in WarehouseInfo.__table__.columns} for w in warehouse_infos]

    print(" Warehouses loaded: ", warehouse_dicts)  
    
    return render_template('home/home.html', warehouse_infos=warehouse_infos)

@home_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login_bp.login_page'))  

@home_bp.route("/privacy")
def privacy():
    return render_template("home/privacy.html")

@home_bp.route("/error")
def error():
    return render_template("shared/error.html", request_id="Error 404")


