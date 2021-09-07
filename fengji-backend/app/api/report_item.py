# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-09-07

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required, get_current_user

bp = Blueprint('report_item', __name__, url_prefix='/api/report_item')


@bp.route('/', methods={'POST'})
@jwt_required()
def add_report_item():
    pass


@bp.route('/', methods={'DELETE'})
@jwt_required()
def delete_report_item():
    pass


@bp.route('/', methods={'GET'})
@jwt_required()
def get_report_item():
    pass


@bp.route('/', methods={'PUT'})
@jwt_required()
def modify_report_item():
    pass