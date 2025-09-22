from flask import Flask
from flask_session import Session
from .config import config
from .context_processors import inject_global_variables

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Session management
    Session(app)

    # Register context processors
    app.context_processor(inject_global_variables)

    # Register blueprints (will be done by AI-B)
    # from .routes.auth import auth_bp
    # from .routes.dashboard import dashboard_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(dashboard_bp)

    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {"status": "error", "error": "Resource not found", "code": "NOT_FOUND"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"status": "error", "error": "Internal server error", "code": "INTERNAL_ERROR"}, 500

    return app