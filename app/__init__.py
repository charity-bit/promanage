from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Configuration

    from config import config_options
    app.config.from_object(config_options[config_name])

    # Register Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initialize flask extensions

    bootstrap.init_app(app)


    return app