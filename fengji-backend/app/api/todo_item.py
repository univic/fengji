import json
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_current_user, current_user
from app.model.todo_item import TodoItem
from app.model.report_group import ReportGroup
from app.model.post_forms import TodoItemForm

bp = Blueprint('todo_item', __name__, url_prefix='/api/todo_item')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_todo_item():
    form = TodoItemForm(request)
    if form.validate():
        new_todo_item = TodoItem()
        new_todo_item.title = form.title.data
        report_group = ReportGroup.objects(id=form.report_group.data, creator=get_current_user().id).first()
        new_todo_item.report_group = report_group
        new_todo_item.creator = get_current_user()
        try:
            new_todo_item.save()
            response = jsonify({
                        'status': 'success',
                        'messages': ['new item added'],
                        'id': str(new_todo_item.id)
                        })
        except Exception as e:
            print(e)
            response = jsonify({
                        'status': 'error',
                        'messages': [e],
                    })
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
    return response


@bp.route('/', methods={'GET'})
@jwt_required()
def get_todo_item():
    response = None
    if request.args['type'] == 'all':
        # return detailed info all all record items
        try:
            todo_item_list = []
            todo_items = TodoItem.objects()
            for item in todo_items:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = json.loads(item.to_json())
                # turn id into str format, turn datetime obj into timestamp
                item_dict["id"] = str(item.id)
                item_dict.pop("_id")
                todo_item_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'todo_item_list': todo_item_list
            }
        except Exception as e:
            print(e)
            response = {
                'status': 'error',
                'messages': [e]
            }
    elif request.args['type'] == 'my':
        output_list = []
        my_todo_list = TodoItem.objects(creator=current_user.id)
        for item in my_todo_list:
            output_list.append(item.to_json())
        response = {
            'status': 'success',
            'messages': [''],
            'todo_item_list': output_list
        }
    return response


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_todo_item():
    todo_item = TodoItem.objects(id=request.args['id'], creator=current_user.id)
    try:
        todo_item.delete()
        response = {
            'status': 'success',
            'messages': ['条目已删除']
        }
    except Exception as e:
        print(e)
        response = {
            'status': 'error',
            'messages': [e]
        }
    return response


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_todo_item():
    form = TodoItemForm(request.form, meta={'csrf': False})
    if form.validate():
        item = TodoItem.objects(id=request.args['id'], creator=current_user.id)
        try:
            response = {
                'status': 'success',
                'messages': ['条目已删除']
            }
        except Exception as e:
            response = {
                'status': 'error',
                'messages': [e]
            }
    else:
        error_status = list(form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]
        # construct the return data
        response = {
            'status': 'error',
            'messages': error_status
        }

    return response
