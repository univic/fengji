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

    def to_json(self, recursive_search, with_tags):
        raw_data = self
        # convert mongodb object to dict, replace _id
        item_dict = db_util.dbo_better_json(raw_data)

        output_dict = self.convert_refs(item_dict)
        return output_dict

    def convert_refs(self, data):
        data["create_time"] = int(data.create_time.timestamp())
        # convert the creator reference field to a json readable format
        data['creator'] = {
            'id': str(self.creator.id),
            'username': self.creator.username
        }
        data['parent_group'] = {
            'id': str(self['parent_group']),
        }
        data['member_user'] = []
        return data
