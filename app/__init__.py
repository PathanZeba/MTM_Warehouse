from flask import Flask, g
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_from_directory
import os
# Extensions ko global define karo
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)

    # Extensions ko initialize karo
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "login_bp.login_page"

    with app.app_context():
        # Models ko import karo
        from app.models.user import User
        from app.models import LoginEmp, WarehouseInfo

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(user_id)

        # Services initialize karo
        from app.services.warehouse_service_impl import WarehouseService
        from app.services.list_page_count_service import ListPageCountService

        app.warehouse_service = WarehouseService()
        app.list_page_count_service = ListPageCountService(0, 0, 0)

    # Blueprints ko register karo
    from app.routes.home import home_bp
    from app.routes.login import login_bp
    from app.routes.register import register_bp
    from app.routes.access_denied import account_bp
    from app.routes.action import action_bp
    from app.routes.report_page import report_bp
    from app.routes.warehouse import warehouse_bp
    
    

    app.register_blueprint(home_bp, url_prefix="/home")
    app.register_blueprint(login_bp, url_prefix="/MTM")
    app.register_blueprint(register_bp, url_prefix="/MTM")
    app.register_blueprint(account_bp, url_prefix="/MTM")
    app.register_blueprint(action_bp, url_prefix="/MTM")
    app.register_blueprint(report_bp, url_prefix="/MTM")
    app.register_blueprint(warehouse_bp, url_prefix="/warehouse")
    

    # Before request function to store logged-in user in `g`
    @app.before_request
    def load_logged_in_user():
        if current_user.is_authenticated:
            g.user = current_user
        else:
            g.user = None

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)


     # Favicon route fix
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.commit()  # Ensure transactions are committed
        db.session.remove()


    
    return app  # Yeh sahi tarika hai return karne ka
