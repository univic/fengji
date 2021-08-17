import traceback
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.tag_template_group import TagGroup
from app.model.post_forms import TagGroupForm

# TODO: need a get my report groups api
# TODO: need a free to join filter
# TODO: reconstruct GET method

bp = Blueprint('tag_group', __name__, url_prefix='/api/tag_group')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_tag_group():
    tag_group_form = TagGroupForm(request.form, meta={'csrf': False})
    print(request.form)
    if tag_group_form.validate():
        new_tag_group = TagGroup()
        tag_group_creator = get_current_user()
        new_tag_group.tag_group_name = tag_group_form.tag_group_name.data
        new_tag_group.tag_group_color = tag_group_form.tag_group_color.data
        new_tag_group.tag_group_creator = tag_group_creator
        try:
            new_tag_group.save()
            response = {
                'status': 'success',
                'messages': ['标签组添加成功~'],
                'id': str(new_tag_group.id)
            }
        # if the group name is not unique, let the frontend know
        except NotUniqueError:
            response = {
                'status': 'error',
                'messages': ['重复的标签组名']
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
        error_status = list(tag_group_form.errors.values())
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
def get_tag_group():
    if request.args['type'] == 'all':
        # return detailed info of all groups
        try:
            tag_group_list = []
            tag_groups = TagGroup.objects()
            for item in tag_groups:
                item_json = item.to_json()
                tag_group_list.append(item_json)
            response = {
                'status': 'success',
                'messages': [''],
                'tag_group_list': tag_group_list
                }
        except Exception as e:
            print(traceback.print_exc())
            response = {
                    'status': 'error',
                    'messages': [e.args[0]]
                }
    elif request.args['type'] == 'check_existence':
        tag_group = TagGroup.objects(tag_group_name=request.args['tag_group_name'])
        if not tag_group:
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
def delete_tag_group():
    tag_group = TagGroup.objects(id=request.args['id'])
    try:
        tag_group.delete()
        response = {
            'status': 'success',
            'messages': ['标签组已删除']
        }
    except Exception as e:
        response = {
            'status': 'error',
            'messages': [e]
        }
    return response


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_tag_group():
    tag_group_form = TagGroupForm(request.form, meta={'csrf': False})
    if tag_group_form.validate():
        tag_group = TagGroup.objects(id=tag_group_form.id.data).first()
        tag_group.tag_group_name = tag_group_form.tag_group_name.data
        tag_group.tag_group_color = tag_group_form.tag_group_color.data
        try:
            tag_group.save()
            response = {
                'status': 'success',
                'messages': ['标签组修改成功~']
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
        error_status = list(tag_group_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)
