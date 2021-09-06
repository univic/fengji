# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-09-06

"""
Custom Validators for WTForms
"""

from wtforms import ValidationError


def check_mongo_oid():
    message = '无效的对象ID'

    def _check_mongo_oid(form, field):
        oid = field.data
        if len(oid) != 12:
            raise ValidationError(message)

    return _check_mongo_oid
