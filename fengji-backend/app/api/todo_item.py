import json
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_current_user, current_user
from app.model.todo_item import TodoItem
from app.model.report_group import ReportGroup

bp = Blueprint('todo_item', __name__, url_prefix='/api/todo_item')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_todo_item():
    new_todo_item = TodoItem()
    post_data = request.get_json()
    new_todo_item.title = post_data['title']
    report_group = ReportGroup.objects(id=post_data['report_group'], creator=get_current_user().id).first()

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
