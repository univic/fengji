import datetime
from mongoengine import StringField, ReferenceField, DateTimeField, EmbeddedDocumentListField, FileField, ListField, \
    BooleanField
from app.model.report_group import ReportGroup
from app.model.tag_template import TodoItemTag
from app.model.user_model import User
from app.lib.database import db
import app.utilities.db_util as db_util


class TodoItem(db.Document):
    title = StringField(required=True)
    tag_list = EmbeddedDocumentListField(TodoItemTag)
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
    completion_flag = BooleanField(default=False, required=True)
    status = StringField()
    owner = ReferenceField(User)
    report_group = ReferenceField(ReportGroup, required=True)
    start_time = DateTimeField()
    planned_finish_time = DateTimeField()
    actual_finish_time = DateTimeField()
    description = StringField()
    attachment = FileField()

    def to_json(self):
        output_dict = db_util.dbo_better_json(self)
        output_dict = self.convert_refs(output_dict)
        return output_dict

    def convert_refs(self,  output_dict):
        # convert the creator reference field to a json readable format
        output_dict['creator'] = self['creator'].to_json()
        output_dict['report_group'] = self['report_group'].to_json(recursive_search=True, with_descendant=True)
        return output_dict

