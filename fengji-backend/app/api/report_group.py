import json
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.report_group import ReportGroup
from app.model.post_forms import ReportGroupForm

bp = Blueprint('report_group', __name__, url_prefix='/api/report_group')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_report_group():
    report_group_form = ReportGroupForm(request.form, meta={'csrf': False})
    if report_group_form.validate():
        new_group = ReportGroup()
        group_creator = get_current_user()
        new_group.group_name = report_group_form.group_name.data
        new_group.is_project = report_group_form.is_project.data
        new_group.group_color = report_group_form.group_color.data
        new_group.group_creator = group_creator
        try:
            new_group.save()
            response = {
                'status': 'success',
                'messages': ['报告组添加成功~']
            }
        # if the tag name is not unique, let the frontend know
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
