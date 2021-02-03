# -*- coding: utf-8 -*-
# Author : univic
# Date: 2021-02-03

from flask import Blueprint, request

bp = Blueprint('accounts', __name__, url_prefix='/api/accounts')


def get_csrf_token():
    pass