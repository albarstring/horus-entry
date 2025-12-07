from flask import Flask
from app.config import Config
from app.extensions import cors, db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    cors.init_app(app)
    db.init_app(app)
    
    # Register blueprints
    from app.routes.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')
    
    return app

