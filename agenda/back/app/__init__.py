from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import User, Task

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.auth.ruotes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.tareas.ruotes import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/api')

    return app