from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options,Config

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # app Configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    # initializing flask extensions
    bootstrap.init_app(app)

    from .requests import request_config
    request_config(app)

    # Registering Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

    