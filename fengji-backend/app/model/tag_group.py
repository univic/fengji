from bson import json_util
import datetime
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField


class TagGroup(db.Document):
    tag_group_name = StringField(required=True, unique=True)
    tag_group_color = StringField()
    tag_group_creator = ReferenceField(User, required=True)
    tag_group_created_at = DateTimeField(default=datetime.datetime.now())

    def to_json(self):
        print('running')
        data = self
        data_dict = data.to_mongo().to_dict()
        data_dict['id'] = str(data_dict['_id'])
        data_dict.pop('_id')
        data2 = data['tag_group_creator'].to_mongo().to_dict()
        data2['id'] = str(data2['_id'])
        data2.pop('_id')
        data_dict['tag_group_creator'] = data2
        return data_dict
