# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

import datetime
from mongoengine.errors import NotUniqueError
from flask import Blueprint, request, jsonify
from flask_mongoengine.wtf import model_form
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies
from app.model.user_model import User
from app.model.post_forms import RegistrationForm, LoginForm
from app.lib.flask_jwt_extended import jwt


bp = Blueprint('user', __name__, url_prefix='/api/user')
SignupForm = model_form(User)


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


@bp.route('/login', methods={'POST'})
def login():
    login_form = LoginForm(request.form, meta={'csrf': False})
    response = jsonify({
        'status': 'error',
        'messages': ['无效的登陆信息']
    })
    if login_form.validate():
        user = User.objects(username=login_form.username.data).first()
        if user and check_password_hash(user.password_hash, login_form.password.data):
            access_token = create_access_token(identity=user)
            response = jsonify({
                'status': 'success',
                'messages': ['登陆成功'],
                'access_token': access_token,
                'user_id': str(user.id),
                'user_name': user.username,
                'user_role': user.user_role,
                'user_status': user.user_status
            })
            set_access_cookies(response, access_token)

    return response


@bp.route('/signup', methods={'POST'})
def signup():
    # instantiate the RegistrationForm, the form and the actual user ORM object is loose coupled
    signup_form = RegistrationForm(request.form, meta={'csrf': False})

    # if the form is validated, continue to create a new user
    if signup_form.validate():
        user = User()
        user.username = signup_form.username.data
        user.email = signup_form.email.data
        user.password_hash = generate_password_hash(signup_form.password.data)     # turn the password into hash
        try:
            user.save()
            ret = {
                'status': 'success',
                'messages': ['注册成功~']
            }

        # if the username is not unique, let the frontend know
        except NotUniqueError:
            ret = {
                'status': 'error',
                'messages': ['重复的用户名']
            }
        # construct the return data

    # if the form can not be validated, return error msg
    else:
        # get error messages from the form.errors dict
        error_status = list(signup_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]

        # construct the return data
        ret = {
            'status': 'error',
            'messages': error_status
        }

    return jsonify(ret)


@bp.route('/check_username_unique', methods=['GET'])
def check_user_existence():
    user = User.objects(username=request.args["username"])
    if not user:
        ret = {
            'status': 'success',
            'messages': ['用户名可用']
        }
    else:
        ret = {
            'status': 'error',
            'messages': ['这一用户名已被注册']
        }
    return jsonify(ret)


@bp.route('/csrf_token')
def get_csrf_token():
    if request.method == "GET":
        return "Ouch"


@jwt_required
@bp.route('/protected', methods=['GET'])
def protected():
    current_user = get_jwt_identity()
    print(current_user.to_pymongo())
    return f"current user is {current_user}"
