import datetime
from app.lib.database import db
from app.model.user_model import User
from app.model.tag_group import TagGroup
import app.utilities.db_util as db_util
from mongoengine import StringField, BooleanField, IntField, EmbeddedDocument, DateTimeField, ReferenceField


class TagTemplate(db.Document):
    tag_template_name = StringField(required=True, unique=True)
    tag_field_type = StringField(required=True)
    tag_group_assignment = ReferenceField(TagGroup, required=True)
    tag_default_value = StringField()
    tag_preview = BooleanField(default=False)
    tag_required = BooleanField(default=False)
    tag_priority = IntField(default=1)
    tag_color = StringField()
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)

    def to_json(self):
        raw_data = self

        # convert mongodb object to dict, replace _id
        item_dict = db_util.dbo_better_json(raw_data)
        item_dict["create_time"] = int(raw_data.create_time.timestamp())
        item_dict['tag_group_assignment'] = {
            'id': str(raw_data.tag_group_assignment.id),
            'tag_group_name': raw_data.tag_group_assignment.tag_group_name
        }
        item_dict["creator"] = {
                    'id': str(raw_data.creator.id),
                    'username': raw_data.creator.username
                }
        return item_dict


class ReportGroupTagTemplate(db.Document):
    tag_template_name = StringField(required=True, unique=True)


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
