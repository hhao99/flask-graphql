# system lib
import logging
import os
from logging.handlers import RotatingFileHandler
# flask lib
from flask import Flask

# local lib
from app.config import Config

def create_app(config_class=Config):

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config_class)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app