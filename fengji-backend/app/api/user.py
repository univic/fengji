# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

import datetime
from flask import Blueprint, request, jsonify
from flask_mongoengine.wtf import model_form
from werkzeug.security import generate_password_hash
from app.lib.database import db
from app.model.user_model import User
from app.model.post_forms import RegistrationForm


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


@bp.route('/login')
def login():
    if request.method == 'POST':
        pass
    return 'user/login'


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
        user.save()

        # construct the return data
        ret = {
            'status': 'success',
            'msg': '注册成功'
        }

    # if the form can not be validated, return error msg
    else:
        # get error messages from the form.errors dict
        error_status = list(signup_form.errors.values())
        for i, item in enumerate(error_status):
            error_status[i] = item[0]

        # construct the return data
        ret = {
            'status': 'error',
            'errors': error_status
        }
        print(ret)

    return jsonify(ret)


@bp.route('/csrf_token')
def get_csrf_token():
    if request.method == "GET":
        return "Ouch"
