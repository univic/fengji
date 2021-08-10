import json
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.report_group import ReportGroup
from app.model.post_forms import ReportGroupForm

# TODO: need a get my report groups api
# TODO: need a free to join filter
# TODO: reconstruct GET method

bp = Blueprint('report_group', __name__, url_prefix='/api/report_group')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_report_group():
    report_group_form = ReportGroupForm(request.form, meta={'csrf': False})
    if report_group_form.validate():
        new_report_group = ReportGroup()
        group_creator = get_current_user()
        new_report_group.name = report_group_form.name.data
        new_report_group.color = report_group_form.color.data
        new_report_group.creator = group_creator
        try:
            new_report_group.save()
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
        error_status = list(report_group_form.errors.values())
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
def get_report_group():
    if request.args['type'] == 'all':
        # return detailed info of all groups
        try:
            report_group_list = []
            report_groups = ReportGroup.objects()
            for item in report_groups:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = json.loads(item.to_json())
                # turn id into str format, turn datetime obj into timestamp
                item_dict["id"] = str(item.id)
                item_dict["created_at"] = int(item.created_at.timestamp())
                item_dict.pop("_id")
                # get group_creator info
                group_creator = item.creator
                group_creator_dict = {
                    'id': str(group_creator.id),
                    'username': group_creator.username
                }
                item_dict["group_creator"] = group_creator_dict
                report_group_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'group_list': report_group_list
                }
        except Exception as e:
            print(e)
            response = {
                    'status': 'error',
                    'messages': [e.args[0]]
                }
    elif request.args['type'] == 'check_existence':
        report_group = ReportGroup.objects(group_name=request.args['group_name'])
        if not report_group:
            response = {
                'status': 'success',
                'messages': ['组名可用'],
            }
        else:
            response = {
                'status': 'error',
                'messages': ['组名已存在'],
            }
    # return all the report groups created by current user
    elif request.args['type'] == 'my':
        pass
    else:
        response = {
            'status': 'error',
            'message': '错误的请求参数',
        }
        return response, 400
    return response


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_report_group():
    report_group = ReportGroup.objects(id=request.args['id'])
    try:
        report_group.delete()
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
def modify_report_group():
    report_group_form = ReportGroupForm(request.form, meta={'csrf': False})
    if report_group_form.validate():
        report_group = ReportGroup.objects(id=report_group_form.id.data).first()
        report_group.group_name = report_group_form.group_name.data
        report_group.tag_required = report_group_form.tag_required.data
        report_group.group_color = report_group_form.group_color.data
        try:
            report_group.save()
            response = {
                'status': 'success',
                'messages': ['报告组修改成功~']
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
        error_status = list(report_group_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)
