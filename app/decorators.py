from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def superuser_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login_bp.login_page"))  
        
        if not getattr(current_user, 'role', None) == 'super_user':
            
            
            return f(*args, **kwargs)
        
        return f(*args, **kwargs)
    return decorated_function

def masteruser_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login_bp.login_page"))  

        if not getattr(current_user, 'role', None) == 'master_user':
            
            
            return f(*args, **kwargs)

        return f(*args, **kwargs)
    return decorated_function