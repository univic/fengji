import datetime
from app.lib.database import db
from app.model.user_model import User
from app.model.item_tag import ReportGroupTag
from mongoengine import StringField, EmbeddedDocumentListField, DateTimeField, ReferenceField, ListField, EmbeddedDocument


class ReportGroup(db.Document):
    """
    20 - active
    99 - locked
    """
    # a walk around for self referencing
    def __new__(cls):
        cls.group_name = StringField(required=True, unique=True)
        cls.group_color = StringField()
        cls.group_created_at = DateTimeField(default=datetime.datetime.now())
        cls.group_creator = ReferenceField(User, required=True)
        cls.group_members = EmbeddedDocumentListField(ReportGroupMember)
        cls.sub_group = ListField(ReferenceField(cls))
        cls.group_status = ListField(StringField())
        return object.__new__(cls)


class MemberRole(db.Document):
    role_code = StringField(required=True)
    role_name = StringField(required=True, unique=True)
    role_description = StringField()


class ReportGroupMember(EmbeddedDocument):
    user = ReferenceField(User)
    role = ListField(ReferenceField(MemberRole))
