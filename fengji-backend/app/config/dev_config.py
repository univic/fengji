# -*- coding: utf-8 -*-
# Author : univic

import datetime
from app.config import BaseConfig


class DevConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=8)
