# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-09-07

import datetime
from mongoengine import StringField, ReferenceField, DateTimeField, EmbeddedDocumentListField, FileField, ListField, \
    BooleanField
from app.lib.database import db
from app.model.user_model import User


class ReportItem(db.Document):
    title = StringField(required=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
