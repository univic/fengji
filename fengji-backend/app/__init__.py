# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from flask import Flask
from app.utilities.logger import create_logger
from app.config import app_config
from app.api import register_blueprint
from app.extensions import config_extensions

logger = create_logger()


def create_app():
    app = Flask(__name__)
    app.debug = True
    register_blueprint(app)
    config_extensions()
    return app
