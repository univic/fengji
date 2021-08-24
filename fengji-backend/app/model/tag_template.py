import datetime
from app.lib.database import db
from app.model.user_model import User
from app.model.tag_template_group import TagTemplateGroup
import app.utilities.db_util as db_util
from mongoengine import StringField, BooleanField, IntField, EmbeddedDocument, DateTimeField, ReferenceField


class TagTemplate(db.Document):
    tag_template_name = StringField(required=True, unique=True)
    tag_field_type = StringField(required=True)
    tag_group_assignment = ReferenceField(TagTemplateGroup, required=True)
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
            'name': raw_data.tag_group_assignment.name
        }
        item_dict["creator"] = {
                    'id': str(raw_data.creator.id),
                    'username': raw_data.creator.username
                }
        return item_dict


class ItemTag(EmbeddedDocument):
    tag_field_value = StringField()
    tag_name = StringField(required=True)
    tag_field_type = StringField(required=True)
    tag_default_value = StringField()
    tag_for_preview = BooleanField(default=False)
    tag_priority = IntField(default=1)
    tag_color = StringField()
    tag_created_at = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
    ref_tag_template = ReferenceField(TagTemplate, required=True)


class ReportGroupTagTemplate(db.Document):
    tag_template_name = StringField(required=True, unique=True)


class ReportGroupTag(EmbeddedDocument):
    tag_template_name = StringField(required=True, unique=True)
    ref_tag_template = ReferenceField(ReportGroupTagTemplate, required=True)


