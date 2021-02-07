# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03


class BaseConfig(object):
    SECRET_KEY = "q4qb@KYP$4&aUy@!YcNvd^bfb4SxaGz$"
    USE_CONFIG = 'DEV'
    LOGGING = {
        'MAX_LOG_SIZE': 512,    # in KBytes
        'BACKUP_COUNT': 1
    }
    # mongodb 配置
    MONGODB_SETTINGS = {
        'db': 'fengji',
        'host': 'mongodb://localhost:27017/',
        'port': 27017
    }


def get_config():
    if BaseConfig.USE_CONFIG == 'DEV':
        from app.config.dev_config import DevConfig
        return DevConfig
    elif BaseConfig.USE_CONFIG == 'PRODUCTION':
        from app.config.production_config import ProductionConfig
        return ProductionConfig
    # import app.config.flask_security_config


app_config = get_config()

