from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from app import db
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.models.login_emp import LoginEmp
from app.forms import RegisterForm

register_bp = Blueprint('register_bp', __name__, url_prefix='/MTM')

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'GET':
        login_emps = LoginEmp.query.filter((LoginEmp.Username == None) | (LoginEmp.Username == "")).all()
        return render_template('login/register.html', form=form, login_emps=login_emps)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        manager_id = form.manager_id.data
        selected_role = form.selected_role.data

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect(url_for('register_bp.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        new_user = User(username=username, password_hash=hashed_password, role=selected_role)
        db.session.add(new_user)

        emp = LoginEmp.query.filter_by(id=manager_id).first()
        if not emp:
            flash("Invalid Manager ID!", "danger")
            return redirect(url_for('register_bp.register'))

        emp.username = username
        db.session.add(emp)

        try:
            db.session.commit()
            flash("Registration successful!", "success")
            return redirect(url_for('login_bp.login_page'))
        except Exception as e:
            db.session.rollback()
            flash("Database error! Try again.", "danger")
            return redirect(url_for('register_bp.register'))

    return render_template('login/register.html', form=form)
