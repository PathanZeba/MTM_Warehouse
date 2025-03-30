from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from app.models import user
from app.models.warehouse_info import WarehouseInfo
from app import db

#  Blueprint correctly defined
home_bp = Blueprint("home_bp", __name__, url_prefix="/home")

@home_bp.route("/")
@login_required
def home_page():
    # Fetch warehouse data from database
    warehouse_infos = WarehouseInfo.query.all()

    # Debugging: Check warehouse IDs
    if not warehouse_infos:
        print(" No warehouse found in DB!")
    else:
        print(" Warehouses loaded: ", [w.warehouse_info_id for w in warehouse_infos])

    return render_template("home/home.html", warehouses=warehouse_infos, user=current_user)

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


