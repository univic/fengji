# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-07-18

import datetime
import app.utilities.db_util as db_util
from app.lib.database import db
from app.model.user_model import User
import app.model.tag_template
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField


class TagTemplateGroup(db.Document):
    name = StringField(required=True, unique=True)
    color = StringField()
    creator = ReferenceField(User, required=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    parent_group = ReferenceField('self')
    child_group = ListField(ReferenceField('self'))

    def to_json(self, recursive_search, with_tags):

        data = self
        output_dict = db_util.dbo_better_json(data)

        # use recursive search to go through the tree structure
        if data.child_group != [] and recursive_search:
            child_group_list = []
            for element in data.child_group:
                # for each reference element(TagTemplateGroup), call to_json method again
                child_group_dict = element.to_json(recursive_search=True, with_tags=with_tags)
                child_group_list.append(child_group_dict)
            # convert mongodb object to dict, replace _id
            output_dict['child_group'] = child_group_list
        elif not data.child_group:
            # remove the empty array, otherwise the frontend cascader will have a residual panel.
            output_dict['child_group'] = None

        # get related tag template list
        if with_tags:
            tag_template_list = []
            result = app.model.tag_template.TagTemplate.objects(tag_group_assignment=data.id)
            for element in result:
                tag_template_list.append(element.to_json())
            output_dict['tag_template_list'] = tag_template_list

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
