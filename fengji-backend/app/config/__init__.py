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
    # user config
    USER_SETTINGS = {
        'MIN_USERNAME_LENGTH': 3,
        'MAX_USERNAME_LENGTH': 25,
        'MIN_PWD_LENGTH': 8,
        'MAX_PWD_LENGTH': 32,
    }
    # tag config
    TAG_SETTINGS = {
        'MIN_TAG_NAME_LENGTH': 2,
        'MAX_TAG_NAME_LENGTH': 10,
        'ALLOWED_TAG_TYPES': ['simple', 'select', 'text', 'number']
    }
    # report group config
    REPORT_GROUP_SETTINGS = {
        'MIN_GROUP_NAME_LENGTH': 3,
        'MAX_GROUP_NAME_LENGTH': 50,
        'MIN_ROLE_NAME_LENGTH': 2,
        'MAX_ROLE_NAME_LENGTH': 8,
        'MAX_DESC_LENGTH': 20,
        'MIN_ROLE_ABBR_LENGTH': 2,
        'MAX_ROLE_ABBR_LENGTH': 5,
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

