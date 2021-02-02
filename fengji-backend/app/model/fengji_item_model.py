from mongoengine import StringField, ReferenceField, ListField, EmbeddedDocumentListField
from app.model.user_model import User


class BasicItem(object):

    def __init__(self):
        self.item_id = None
        self.item_title = StringField(required=True)
        self.tag_list = EmbeddedDocumentListField()
        self.created_at = None
        self.created_by = ReferenceField(User)
