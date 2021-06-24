import json
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.model.fengji_item_model import BasicItem

bp = Blueprint('item', __name__, url_prefix='/api/item')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_record_item():
    new_record_item = BasicItem()
    print(request.data)
    post_data = request.get_json()
    new_record_item.item_title = post_data['item_title']
    try:
        new_record_item.save()
        response = jsonify({
                    'status': 'success',
                    'messages': ['new item added'],
                    'id': str(new_record_item.id)
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
def get_record_item():
    response = None
    if request.args['type'] == 'all':
        # return detailed info all all record items
        try:
            record_item_list = []
            record_items = BasicItem.objects()
            for item in record_items:
                # convert the mongodb query obj to json, then load it into dict
                # make id, date and user more readable before return it
                item_dict = json.loads(item.to_json())
                # turn id into str format, turn datetime obj into timestamp
                item_dict["id"] = str(item.id)
                item_dict.pop("_id")
                record_item_list.append(item_dict)
            response = {
                'status': 'success',
                'messages': [''],
                'record_item_list': record_item_list
            }
        except Exception:
            pass
        return response


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_record_item():
    record_item = BasicItem.objects(id=request.args['id'])
    try:
        record_item.delete()
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
