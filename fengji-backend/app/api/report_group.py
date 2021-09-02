import traceback
from mongoengine.errors import NotUniqueError, ValidationError
from mongoengine.queryset.visitor import Q
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, get_current_user
from app.model.report_group import ReportGroup
from app.model.user_model import User
from app.model.post_forms import ReportGroupForm

bp = Blueprint('report_group', __name__, url_prefix='/api/report_group')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_report_group():
    report_group_form = ReportGroupForm(request.form, meta={'csrf': False})
    if report_group_form.validate():
        new_report_group = ReportGroup()
        new_report_group.name = report_group_form.name.data
        new_report_group.color = report_group_form.color.data
        new_report_group.open_join = report_group_form.open_join.data
        current_user = get_current_user()
        new_report_group.creator = current_user
        new_report_group.report_to_user = [current_user]
        try:
            new_report_group.save()
            response = {
                'status': 'success',
                'messages': ['报告组添加成功~']
            }
        # if the group name is not unique, let the frontend know
        except NotUniqueError as e:
            response = {
                'status': 'error',
                'messages': ['重复的报告组名']
            }
            print(traceback.print_exc())
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
        # TODO: search from a root node
        try:
            report_group_list = []
            report_groups = ReportGroup.objects()
            for item in report_groups:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = item.to_json(recursive_search=True, with_descendant=request.args['with_descendant'])
                report_group_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'group_list': report_group_list
                }
        except Exception as e:
            print(traceback.print_exc())
            response = {
                    'status': 'error',
                    'messages': [e.args[0]]
                }
    elif request.args['type'] == 'check_existence':
        report_group = ReportGroup.objects(name=request.args['name'])
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
        user = get_current_user()
        # use Q object to combine a number of constraints
        user_report_groups = ReportGroup.objects(Q(creator=user) | Q(member_user=user) | Q(report_to_user=user))
        report_group_list = []
        # find the top nodes
        for item in user_report_groups:
            # a dict which key is the id of the parent node, and value is the id of its' parent node
            parent_dict = {}
            member_node_list = []
            if item.id in member_node_list:
                # if current item is a known child node, just leave it
                pass
            else:
                if item.id in parent_dict.keys():
                    # if current item is a known parent node, replace the previously logged node
                    for i, element in enumerate(report_group_list):
                        if element.id == parent_dict[item.id]:
                            report_group_list.pop(i)
                            parent_dict.pop(item.id)
                            break
                # if the id of current item does not exist in the either dict, log it as a parent node
                report_group_list.append(item)
                if item.member_node:
                    member_node_list += item.member_node
                if item.parent_node:
                    parent_dict[item.parent_node.id] = item.id
        # get serialized content, use list comprehensions
        output_list = [item.to_json(recursive_search=True, with_descendant=request.args['with_descendant'])
                       for item in report_group_list]

        response = {
            'status': 'success',
            'messages': [''],
            'report_group_list': output_list
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
        report_group.name = report_group_form.name.data
        report_group.open_join = report_group_form.open_join.data
        report_group.color = report_group_form.color.data
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
