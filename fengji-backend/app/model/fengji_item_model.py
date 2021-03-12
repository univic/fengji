import datetime
from mongoengine import StringField, ReferenceField, DateTimeField, EmbeddedDocumentListField, FileField
from app.model.item_tag import ItemTag

from app.model.user_model import User
from app.lib.database import db


class BasicItem(db.Document):
    item_title = StringField(required=True)
    tag_list = EmbeddedDocumentListField(ItemTag)
    created_at = DateTimeField(default=datetime.datetime.now())
    created_by = ReferenceField(User)
    start_time = DateTimeField()
    end_time = DateTimeField()
    description = StringField()
    attachment = FileField()
