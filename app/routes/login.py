from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from app import db
from werkzeug.security import check_password_hash
from app.models.user import User
from uuid import UUID

login_bp = Blueprint('login_bp', __name__, url_prefix='/MTM')


@login_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Debug: Login Attempt - Username={username}, Password={password}")

        user = User.query.filter_by(Username=username).first()

        if user:
            print(f"Debug: Stored Hash = {user.PasswordHash}")
            if check_password_hash(user.PasswordHash, password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for('home_bp.home_page'))  
            else:
                print("Debug: Password did not match")

        flash("Invalid username or password", "danger")

    return render_template('login/login.html')

def fetch_all_login_details():
    users = User.query.all()
    user_details = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_details)  

@login_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login_bp.login_page'))  

@login_bp.route('/access_denied')
def access_denied():
    return render_template('login/access_denied.html')

@login_bp.route('/fetch_login_details', methods=['GET'])
def fetch_all_login_details():
    users = User.query.all()
    user_details = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_details)
