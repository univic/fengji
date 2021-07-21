# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-07-18

import datetime
import app.utilities.db_util as db_util
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField


class TagGroup(db.Document):
    tag_group_name = StringField(required=True, unique=True)
    tag_group_color = StringField()
    tag_group_creator = ReferenceField(User, required=True)
    tag_group_created_at = DateTimeField(default=datetime.datetime.now())

    def to_json(self):
        tag_group_data = self

        # convert mongodb object to dict, replace _id
        tag_group_dict = db_util.dbo_better_json(tag_group_data)
        tag_group_dict['tag_group_creator'] = {
            'id': str(tag_group_data.tag_group_creator.id),
            'username': tag_group_data.tag_group_creator.username
        }
        return tag_group_dict
