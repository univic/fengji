# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

from flask import Blueprint, request
from app.lib.database import db
from app.model.user_model import User

bp = Blueprint('user', __name__, url_prefix='/api/user')


@bp.route('/')
def user_api():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "PATCH":
        pass


@bp.route('/login')
def login():
    if request.method == 'POST':
        pass
    return 'user/login'


@bp.route('/signup')
def signup():
    pass
