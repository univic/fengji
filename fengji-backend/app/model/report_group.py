import datetime
from app.lib.database import db
from app.model.user_model import User
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField, EmbeddedDocument


class MemberRole(db.Document):
    role_code = StringField(required=True)
    role_name = StringField(required=True, unique=True)
    role_description = StringField()


class ReportGroupMember(EmbeddedDocument):
    user = ReferenceField(User)
    role = ListField(ReferenceField(MemberRole))


class ReportGroupTag(EmbeddedDocument):
    tag_name = StringField(required=True)
    tag_color = StringField()
    tag_created_at = DateTimeField(default=datetime.datetime.now())
    tag_created_by = ReferenceField(User, required=True)


class ReportGroup(db.Document):
    """
    20 - active
    99 - locked
    """
    group_name = StringField(required=True, unique=True)
    group_color = StringField()
    group_created_at = DateTimeField(default=datetime.datetime.now())
    group_creator = ReferenceField(User, required=True)
    group_members = EmbeddedDocumentListField(ReportGroupMember)
    group_status = ListField(StringField())
    sub_group = None


# a walk around for self referencing
ReportGroup.sub_group = ListField(ReferenceField(ReportGroup))

