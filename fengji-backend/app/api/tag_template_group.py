import traceback
from mongoengine.errors import NotUniqueError, ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user, get_current_user
from app.model.tag_template_group import TagTemplateGroup
from app.model.post_forms import TagTemplateGroupForm

# TODO: need a get my report groups api
# TODO: need a free to join filter
# TODO: reconstruct GET method

bp = Blueprint('tag_template_group', __name__, url_prefix='/api/tag_template_group')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_tag_template_group():
    form = TagTemplateGroupForm(request.form, meta={'csrf': False})
    if form.validate():
        new_item = TagTemplateGroup()
        new_item.name = form.name.data
        new_item.color = form.color.data
        if form.parent_group.data is not '':
            new_item.parent_group = TagTemplateGroup(id=form.parent_group.data)
        new_item.creator = get_current_user()
        try:
            new_item.save()
            response = {
                'status': 'success',
                'messages': ['标签组添加成功~'],
                'id': str(new_item.id)
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
        error_status = list(form.errors.values())
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
def get_tag_template_group():
    if request.args['type'] == 'all':
        # return detailed info of all groups
        try:
            tag_group_list = []
            root_node = TagTemplateGroup.objects(id='611bc127efb77665894723e6')
            tag_groups = TagTemplateGroup.objects()
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
        tag_group = TagTemplateGroup.objects(name=request.args['name'])
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
    elif request.args['type'] == 'tree':
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
def delete_tag_template_group():
    tag_group = TagTemplateGroup.objects(id=request.args['id'])
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
def modify_tag_template_group():
    form = TagTemplateGroup(request.form, meta={'csrf': False})
    if form.validate():
        item = TagTemplateGroup.objects(id=form.id.data).first()
        item.name = form.name.data
        item.tag_group_color = form.color.data
        try:
            item.save()
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
        error_status = list(form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }
    return jsonify(response)
