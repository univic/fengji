# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-28

import traceback
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from app.model.tag_template import TagTemplate
from app.model.tag_template_group import TagTemplateGroup
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.post_forms import TagTemplateForm

bp = Blueprint('tag_template', __name__, url_prefix='/api/tag_template')


@bp.route('/', methods={'GET'})
@jwt_required()
def get_tag_templates():
    tag_template_list = []
    if request.args['type'] == 'all':
        # return detailed info of all tags
        try:
            tag_templates = TagTemplate.objects()
            for item in tag_templates:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = item.to_json()

                tag_template_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'tag_template_list': tag_template_list
                }
        except Exception as e:
            print(e)
            response = {
                    'status': 'error',
                    'messages': [e.args[0]]
                }
    elif request.args['type'] == 'check_existence':
        tag_template = TagTemplate.objects(name=request.args['name'])
        if not tag_template:
            response = {
                'status': 'success',
                'messages': ['标签名可用'],
            }
        else:
            response = {
                'status': 'error',
                'messages': ['标签名已存在'],
            }
    else:
        response = {
            'status': 'error',
            'message': '错误的请求参数',
        }
        return response, 400
    return response


@bp.route('/', methods={'POST'})
@jwt_required()
def add_tag_template():
    form = TagTemplateForm(request.form, meta={'csrf': False})
    if form.validate():
        new_tag = TagTemplate()
        creator = get_current_user()
        new_tag.name = form.name.data
        new_tag.field_type = form.field_type.data
        tag_template_group = TagTemplateGroup.objects(id=form.tag_group_assignment.data).first()
        new_tag.tag_group_assignment = tag_template_group
        new_tag.default_value = form.default_value.data
        new_tag.preview = form.preview.data
        new_tag.color = form.color.data
        new_tag.creator = creator
        try:
            new_tag.save()
            response = {
                'status': 'success',
                'messages': ['标签添加成功~']
            }
        # if the tag name is not unique, let the frontend know
        except NotUniqueError:
            print(traceback.print_exc())
            response = {
                'status': 'error',
                'messages': ['重复的标签名']
            }
        except ValidationError as e:
            response = {
                'status': 'error',
                'messages': [e.message]
            }
        except Exception as e:
            response = {
                'status': 'error',
                'messages': [e]
            }
    else:
        """
        when validate, WTForms will generate a form.errors dict, which contains all the error messages
        for each form fields, here we get error messages from the form.errors dict, and generate an error info list
        """
        error_status = list(form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_tag_template():
    tag_template = TagTemplate.objects(id=request.args['id'])
    try:
        tag_template.delete()
        response = {
            'status': 'success',
            'messages': ['标签已删除']
        }
    except Exception as e:
        response = {
            'status': 'error',
            'messages': [e]
        }
    return response


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_tag_template():
    form = TagTemplateForm(request.form, meta={'csrf': False})
    if form.validate():
        tag_template = TagTemplate.objects(id=form.id.data).first()
        tag_template.name = form.name.data
        tag_template.field_type = form.field_type.data
        tag_template.default_value = form.default_value.data
        tag_template.preview = form.preview.data
        tag_template.required = form.required.data
        tag_template.color = form.color.data
        try:
            tag_template.save()
            response = {
                'status': 'success',
                'messages': ['标签修改成功~']
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
        error_status = list(form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)
