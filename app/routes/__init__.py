# app/routes/__init__.py
from app import db
from .home import home_bp
from .login import login_bp
from .register import register_bp
from .action import action_bp
from .access_denied import account_bp
from .report_page import report_bp
from .warehouse import warehouse_bp