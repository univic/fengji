# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from flask import Flask
from app.utilities.logger import create_logger
from app.config import app_config
from app.api import register_blueprint
from app.lib.database import db_init
from app.extensions import config_extensions

logger = create_logger()


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(app_config)
    register_blueprint(app)
    db_init(app)
    config_extensions()
    return app
