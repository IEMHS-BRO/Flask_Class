from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required

db = SQLAlchemy()
migrate = Migrate()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    """=== Flask Configuration ==="""
    from .configs import Config
    config = Config()
    app.config.from_object(config)

    """=== Database Init ==="""
    db.init_app(app)
    migrate.init_app(app, db)

    """=== JWT Init ==="""
    jwt.init_app(app)

    """=== Routes Init ==="""
    from .routes import auth_routes, product_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(product_routes.bp)

    return app