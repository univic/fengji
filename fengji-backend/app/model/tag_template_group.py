# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-07-18

import datetime
import app.utilities.db_util as db_util
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField


class TagTemplateGroup(db.Document):
    name = StringField(required=True, unique=True)
    color = StringField()
    creator = ReferenceField(User, required=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    parent_group = ReferenceField('self')
    child_group = ListField(ReferenceField('self'))

    def to_json(self, recursive_search=False):
        data = self

        # use recursive search to go through the tree structure
        if data.child_group and recursive_search:
            child_group_list = []
            for element in data.child_group:
                child_group_dict = element.to_json(recursive_search=True)
                child_group_list.append(child_group_dict)
        # convert mongodb object to dict, replace _id
        output_dict = db_util.dbo_better_json(data)
        output_dict['creator'] = {
            'id': str(data.creator.id),
            'username': data.creator.username
        }
        return output_dict

    def recursive_structure_search(self, data):
        if data.child_group:
            for element in data.child_group:
                item = TagTemplateGroup(id=element.id)
                self.recursive_structure_search(item)

