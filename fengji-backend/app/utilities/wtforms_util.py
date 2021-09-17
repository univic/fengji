# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-09-06

"""
Custom Validators for WTForms
"""
from wtforms import ValidationError, Field, Form
from app.model.post_forms import TodoItemTagForm


def check_mongo_oid():
    message = '无效的对象ID'

    def _check_mongo_oid(form, field):
        oid = field.data
        if len(oid) != 24:
            raise ValidationError(message)

    return _check_mongo_oid


class ExtendedForm(Form):
    """
    Overwrite the init method of WTForms Form class to support application/json data
    if received json data, convert them before call the Form
    Note: this will leave the field's raw_data as null, which cause the InputRequired validation fails
    use DataRequired instead
    """

    def __init__(self, request):
        if "application/json" in request.headers.get("Content-Type"):
            data = request.get_json(silent=True)
            args = request.args.to_dict()
        else:
            data = request.form.to_dict()
            args = request.args.to_dict()
        super(ExtendedForm, self).__init__(data=data, **args)


class TagListField(Field):
    """
    The _value method is called by the TextInput widget to provide the value that is displayed in the form.
    Overriding the process_formdata() method processes the incoming form data back into a list of tags.
    """

    def _value(self):
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [TodoItemTagForm(x) for x in valuelist]
        else:
            self.data = []
