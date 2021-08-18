import datetime
from app.lib.database import db
from app.model.user_model import User
from app.model.tag_template import TagTemplate
import app.utilities.db_util as db_util
from mongoengine import StringField, ListField, BooleanField, IntField, EmbeddedDocument, DateTimeField, ReferenceField


class TagTemplateCollection(db.Document):
    name = StringField(required=True, unique=True)
    tag_template_list = ListField(ReferenceField(TagTemplate))
    create_time = DateTimeField(default=datetime.datetime.now())
    creator = ReferenceField(User, required=True)
