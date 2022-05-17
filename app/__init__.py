from flask import Flask

def create_app(config_name):

    app = Flask(__name__)

    # Configuration

    from config import config_options
    app.config.from_object(config_options[config_name])

    # Register Blueprints

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app