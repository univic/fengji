# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-07-18

import datetime
import app.utilities.db_util as db_util
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField


class TagTemplateGroup(db.Document):
    name = StringField(required=True, unique=True)
    color = StringField()
    creator = ReferenceField(User, required=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    parent_group = ReferenceField('self', required=True)
    direct_descendent_group = ReferenceField('self')

    def to_json(self):
        data = self
        # convert mongodb object to dict, replace _id
        output_dict = db_util.dbo_better_json(data)
        output_dict['creator'] = {
            'id': str(data.creator.id),
            'username': data.creator.username
        }
        return output_dict
