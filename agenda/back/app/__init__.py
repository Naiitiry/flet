from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    from .models import User, Task

    from app.routes import home_bp
    app.register_blueprint(home_bp, url_prefix='/home')
    from app.auth.ruotes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.tareas.ruotes import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/api')

    return app