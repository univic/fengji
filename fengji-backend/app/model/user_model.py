# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from mongoengine import StringField


class User(object):
    def __init__(self):
        self.uid = None
        self.username = StringField(required=True)
        self.password = StringField(required=True)
        self.user_status = None
        self.time_registered = None
        self.employee_id = None
        self.user_role_set = [1]       # 1 for ordinary user, 2 for admin
