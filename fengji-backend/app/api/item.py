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
                    'item_uuid': str(new_record_item.id)
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
    pass
