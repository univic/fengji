# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from mongoengine import StringField, ListField, ReferenceField, EmailField, BooleanField, DateTimeField
from app.model.user_role import UserRole
from app.lib.database import db


class User(db.Document):
    def __init__(self, signup_form):
        self.uid = None
        self.username = StringField(required=True)
        self.email = EmailField()
        self.password = StringField(required=True)
        self.active = BooleanField(default=True)
        self.user_status = None
        self.time_registered = None
        self.confirmed_at = DateTimeField(null=True)
        self.employee_id = None
        self.user_role_set = ListField(ReferenceField(UserRole))

        # Login tracking info
        self.last_login_at = None
        self.last_login_ip = None
        self.current_login_at = None
        self.current_login_ip = None
        self.login_count = 0
