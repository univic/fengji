# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

from app import app_config
import flask_wtf
from app.lib.flask_security import init_flask_security


def config_extensions(app):
    init_flask_security(app)
    flask_wtf.CSRFProtect(app)
    pass

