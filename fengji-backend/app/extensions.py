# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

from app import app_config
from flask_cors import CORS
from app.lib.flask_jwt_extended import jwt


def config_extensions(app):
    CORS(app)
    jwt.init_app(app)
    pass

