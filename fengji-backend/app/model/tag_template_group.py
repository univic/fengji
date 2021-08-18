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
        output_dict = db_util.dbo_better_json(data)

        # use recursive search to go through the tree structure
        if data.child_group != [] and recursive_search:
            child_group_list = []
            for element in data.child_group:
                # for each reference element(TagTemplateGroup), call to_json method again
                child_group_dict = element.to_json(recursive_search=True)
                child_group_list.append(child_group_dict)
            # convert mongodb object to dict, replace _id
            output_dict['child_group'] = child_group_list

        # use convert_refs to convert reference fields to json readable format
        output_dict = self.convert_refs(output_dict)
        return output_dict

    def convert_refs(self, data):
        # convert the creator reference field to a json readable format
        data['creator'] = {
            'id': str(self.creator.id),
            'username': self.creator.username
        }
        if 'parent_group' in data.keys():
            data['parent_group'] = {
                'id': str(self['parent_group']),
            }
        return data

