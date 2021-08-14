import datetime
from mongoengine import StringField, ReferenceField, DateTimeField, EmbeddedDocumentListField, FileField, ListField
from app.model.tag_template import ItemTag
from app.model.report_group import ReportGroup
from app.model.user_model import User
from app.lib.database import db


class TodoItem(db.Document):
    title = StringField(required=True)
    tag_list = EmbeddedDocumentListField(ItemTag)
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
    owner = ReferenceField(User)
    report_group_list = ListField(ReferenceField(ReportGroup, required=True))
    start_time = DateTimeField()
    planned_finish_time = DateTimeField()
    actual_finish_time = DateTimeField()
    description = StringField()
    attachment = FileField()
