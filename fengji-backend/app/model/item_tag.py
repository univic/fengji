from app.lib.database import db
from mongoengine import StringField, BooleanField, IntField


class TagTemplate(db.Document):
    tag_name = StringField(required=True)
    tag_field_type = StringField(required=True)
    tag_field_default_value = StringField()
    # tag_field_editable = BooleanField(default=True)
    tag_for_preview = BooleanField(default=False)
    tag_priority = IntField(default=1)
    tag_color = StringField()


class ItemTag(TagTemplate):
    tag_field_value = StringField()
