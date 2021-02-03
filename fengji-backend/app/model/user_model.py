# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from mongoengine import StringField, ListField, ReferenceField
from app.model.user_role import UserRole


class User(object):
    def __init__(self):
        self.uid = None
        self.username = StringField(required=True)
        self.password = StringField(required=True)
        self.user_status = None
        self.time_registered = None
        self.employee_id = None
        self.user_role_set = ListField(ReferenceField(UserRole))
