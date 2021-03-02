# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-28

import json
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from app.model.item_tag import TagTemplate
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.post_forms import NewTagForm

bp = Blueprint('item_tag', __name__, url_prefix='/api/item_tag')


@bp.route('/', methods={'GET'})
@jwt_required()
def get_tag_templates():
    try:
        tag_template_list = []
        tag_templates = TagTemplate.objects()
        for item in tag_templates:
            # convert the mongodb query obj to json
            # make id, date and user more readable
            tag_template_list.append(json.loads(item.to_json()))
        response = {
            'status': 'success',
            'messages': [''],
            'data': tag_template_list
            }
    except Exception as e:
        print(e)
        response = {
                'status': 'error',
                'messages': [e.args[0]]
            }
    return response


@bp.route('/', methods={'POST'})
@jwt_required()
def add_new_tag():
    new_tag_form = NewTagForm(request.form, meta={'csrf': False})
    if new_tag_form.validate():
        new_tag = TagTemplate()
        tag_creator = get_current_user()
        new_tag.tag_name = new_tag_form.tagName.data
        new_tag.tag_field_type = new_tag_form.tagFieldType.data
        new_tag.tag_field_default_value = new_tag_form.tagDefaultValue.data
        new_tag.tag_preview = new_tag_form.tagPreview.data
        new_tag.tag_color = new_tag_form.tagColor.data
        new_tag.tag_created_by = tag_creator
        try:
            new_tag.save()
            response = {
                'status': 'success',
                'messages': ['标签添加成功~']
            }
        # if the tag name is not unique, let the frontend know
        except NotUniqueError:
            response = {
                'status': 'error',
                'messages': ['重复的标签名']
            }
        except ValidationError as e:
            response = {
                'status': 'error',
                'messages': [e.message]
            }
    else:
        """
        when validate, WTForms will generate a form.errors dict, which contains all the error messages
        for each form fields, here we get error messages from the form.errors dict, and generate an error info list
        """
        error_status = list(new_tag_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)
