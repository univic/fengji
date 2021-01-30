# -*- coding: utf-8 -*-
# Author : univic


from app.config.dev_config import DevConfig


class ProductionConfig(DevConfig):
    # mongodb 配置
    MONGODB_SETTINGS = {
        'db': 'questionnaire',
        'host': 'mongodb://localhost/questionnaire'
    }
    WECHAT = {
        'TOKEN': 'SudeU96aVg5CWh'
    }

    # 生产环境下web端的url
    WEB_BASE_URL = "http://wenjuan.yuzzl.top"

