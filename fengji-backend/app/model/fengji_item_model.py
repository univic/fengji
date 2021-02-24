import datetime
from mongoengine import StringField, ReferenceField, ListField, EmbeddedDocumentListField, DateTimeField
from app.model.user_model import User
from app.lib.database import db


class ItemTag(db.Document):
    pass


class BasicItem(db.Document):
    item_title = StringField(required=True)
    # tag_list = EmbeddedDocumentListField(ItemTag)
    created_at = DateTimeField(default=datetime.datetime.now())
    created_by = ReferenceField(User)
