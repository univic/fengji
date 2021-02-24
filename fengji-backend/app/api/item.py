from flask import Blueprint, request, jsonify
from app.model.fengji_item_model import BasicItem

bp = Blueprint('item', __name__, url_prefix='/api/item')


@bp.route('/', methods={'POST'})
def add_record_item():
    record_item = BasicItem()
    print(request.headers)
    return "Ouch"
