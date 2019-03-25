"""
File::ep_auth.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from flask import Blueprint, request
from werkzeug.security import generate_password_hash

from .tokens import generate_token_with_claims, validate_token
from .db import get_db

import json

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/new', methods=['POST'])
def post_new_user():
    slack_id = request.json.get('slack_id', None)
    password = request.json.get('password', None)

    if slack_id is None or password is None:
        return json.dumps({'msg': 'Either username or password is not entered'}), 400

    get_db().execute('INSERT INTO users VALUES (?, ?, ?)', (slack_id, generate_password_hash(password), False))

    return json.dumps({}), 200


@bp.route('/login', methods=['POST'])
def post_login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username is None or password is None:
        return json.dumps({'msg': 'Either username or password is not entered'}), 400

    print(get_db().execute('SELECT * FROM users WHERE username=?', (username,)).fetchall())

    return_data = {
        'msg': 'Successfully logged in',
        'token': str(generate_token_with_claims({'user_id': 'test'}))
    }

    return json.dumps(return_data), 200


@bp.route('/logout', methods=['POST'])
@validate_token
def post_logout():
    pass