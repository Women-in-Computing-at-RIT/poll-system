"""
File::ep_auth.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from flask import Blueprint, request
from .tokens import generate_token_with_claims, validate_token
from .db import get_db

import json

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/new', methods=['POST'])
def post_new_user():
    pass


@bp.route('/login', methods=['POST'])
def post_login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username is None or password is None:
        return json.dumps({'msg': 'Either username or password is not entered'}), 400

    return_data = {
        'msg': 'Successfully logged in',
        'token': generate_token_with_claims({'user_id': 'test'})
    }

    return json.dumps(return_data), 200


@bp.route('/', methods=['logout'])
@validate_token
def post_logout():
    pass