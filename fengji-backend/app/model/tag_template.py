import datetime
from app.lib.database import db
from app.model.user_model import User
from app.model.tag_group import TagGroup
from mongoengine import StringField, BooleanField, IntField, EmbeddedDocument, DateTimeField, ReferenceField


class TagTemplate(db.Document):
    tag_name = StringField(required=True, unique=True)
    tag_field_type = StringField(required=True)
    tag_group_assignment = ReferenceField(TagGroup, required=True)
    tag_default_value = StringField()
    tag_preview = BooleanField(default=False)
    tag_required = BooleanField(default=False)
    tag_priority = IntField(default=1)
    tag_color = StringField()
    tag_created_at = DateTimeField(default=datetime.datetime.now())
    tag_created_by = ReferenceField(User, required=True)


class ItemTag(EmbeddedDocument):
    tag_field_value = StringField()
    tag_name = StringField(required=True)
    tag_field_type = StringField(required=True)
    tag_default_value = StringField()
    tag_for_preview = BooleanField(default=False)
    tag_priority = IntField(default=1)
    tag_color = StringField()
    tag_created_at = DateTimeField(default=datetime.datetime.now())
    tag_created_by = ReferenceField(User, required=True)
