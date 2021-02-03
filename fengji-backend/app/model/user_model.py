# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-01-31

from mongoengine import StringField, ListField, ReferenceField, EmailField, BooleanField, DateTimeField
from flask_security import UserMixin
from app.model.user_role import UserRole
from app.lib.database import db


class User(db.Document, UserMixin):
    def __init__(self):
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
        self.fs_uniquifier = StringField()
