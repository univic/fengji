import datetime
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField, EmbeddedDocument
from mongoengine import BooleanField


class TagGroup(db.Document):
    tag_group_name = StringField(required=True, unique=True)
    tag_group_color = StringField()
    tag_group_creator = ReferenceField(User, required=True)
    tag_group_created_at = DateTimeField(default=datetime.datetime.now())
