# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

from flask import Blueprint, request
from flask_cors import cross_origin
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


@bp.route('/signup', methods={'POST'})
def signup():
    if request.method == 'POST':
        print('Ouch')


@bp.route('/csrf_token')
def get_csrf_token():
    if request.method == "GET":
        return "Ouch"
