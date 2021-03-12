# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-03-12

import json
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.report_group import GroupMemberRole
from app.model.post_forms import GroupRoleForm

bp = Blueprint('group_role', __name__, url_prefix='/api/group_member_role')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_group_member_role():
    group_role_form = GroupRoleForm(request.form, meta={'csrf': False})
    if group_role_form.validate():
        new_group_role = GroupMemberRole()
        new_group_role.role_name = group_role_form.role_name.data
        new_group_role.role_description = group_role_form.role_description.data
        new_group_role.role_color = group_role_form.role_color.data
        new_group_role.role_creator = get_current_user()
        try:
            new_group_role.save()
            response = {
                'status': 'success',
                'messages': ['报告组添加成功~']
            }
        # if the group name is not unique, let the frontend know
        except NotUniqueError:
            response = {
                'status': 'error',
                'messages': ['重复的报告组名']
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
        error_status = list(group_role_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)


@bp.route('/', methods={'GET'})
@jwt_required()
def get_group_member_role():
    if request.args['type'] == 'all':
        # return detailed info of all groups
        try:
            group_role_list = []
            group_roles = GroupMemberRole.objects()
            for item in group_roles:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = json.loads(item.to_json())
                # turn id into str format, turn datetime obj into timestamp
                item_dict["id"] = str(item.id)
                item_dict["role_created_at"] = int(item.role_created_at.timestamp())
                item_dict.pop("_id")
                # get group_creator info
                role_creator = item.role_creator
                role_creator_dict = {
                    'id': str(role_creator.id),
                    'role_name': role_creator.role_name
                }
                item_dict["role_creator"] = role_creator_dict
                group_role_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'role_list': group_role_list
                }
        except Exception as e:
            print(e)
            response = {
                    'status': 'error',
                    'messages': [e.args[0]]
                }
    elif request.args['type'] == 'check_existence':
        group_role = GroupMemberRole.objects(role_name=request.args['role_name'])
        if not group_role:
            response = {
                'status': 'success',
                'messages': ['角色名可用'],
            }
        else:
            response = {
                'status': 'error',
                'messages': ['角色名已存在'],
            }
    else:
        response = {
            'status': 'error',
            'message': '错误的请求参数',
        }
        return response, 400
    return response


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_report_member_role():
    group_role = GroupMemberRole.objects(id=request.args['id'])
    try:
        group_role.delete()
        response = {
            'status': 'success',
            'messages': ['报告组已删除']
        }
    except Exception as e:
        response = {
            'status': 'error',
            'messages': [e]
        }
    return response


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_report_member_role():
    form = GroupRoleForm(request.form, meta={'csrf': False})
    if form.validate():
        group_role = GroupMemberRole.objects(id=form.id.data).first()
        group_role.group_name = form.group_name.data
        group_role.tag_required = form.tag_required.data
        group_role.group_color = form.group_color.data
        try:
            group_role.save()
            response = {
                'status': 'success',
                'messages': ['报告组角色修改成功~']
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
