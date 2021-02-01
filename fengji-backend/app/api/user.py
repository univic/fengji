from flask import Blueprint, request

bp = Blueprint('user', __name__, url_prefix='/api/user')


@bp.route('/user')
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
    return 'user/login'
