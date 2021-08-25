import datetime
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField, EmbeddedDocument
from mongoengine import BooleanField
from app.lib.database import db
from app.model.user_model import User
import app.utilities.db_util as db_util
from app.model.tag_template import ReportGroupTagTemplate


class ReportGroupMemberRole(db.Document):
    role_abbr = StringField(required=True)
    role_name = StringField(required=True, unique=True)
    role_description = StringField()
    role_creator = ReferenceField(User, required=True)
    role_created_at = DateTimeField(default=datetime.datetime.now())
    role_color = StringField()


class ReportGroupMember(EmbeddedDocument):
    user = ReferenceField(User)
    role = ListField(ReferenceField(ReportGroupMemberRole))


class ReportGroupTag(EmbeddedDocument):
    tag_abbr = StringField(required=True)
    tag_name = StringField(required=True)
    tag_color = StringField()
    tag_created_at = DateTimeField(default=datetime.datetime.now())
    tag_created_by = ReferenceField(User, required=True)


class ReportGroup(db.Document):
    """
    20 - active
    99 - locked
    """
    name = StringField(required=True, unique=True)
    color = StringField()
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
    open_join = BooleanField(default=False)
    member_user = ListField(ReferenceField(User, required=True))
    report_to_user = ListField(ReferenceField(User, required=True))
    parent_node = ReferenceField('self')
    member_node = ListField(ReferenceField('self'))
    status = ListField(StringField())
    tag_list = EmbeddedDocumentListField(ReportGroupTag)
    related_project = StringField()  # should be a reference field, but leave it here for now

    def to_json(self):
        raw_data = self
        # convert mongodb object to dict, replace _id
        item_dict = db_util.dbo_better_json(raw_data)
        item_dict["create_time"] = int(raw_data.create_time.timestamp())
        item_dict["creator"] = {
                    'id': str(raw_data.creator.id),
                    'username': raw_data.creator.username
                }
        return item_dict
