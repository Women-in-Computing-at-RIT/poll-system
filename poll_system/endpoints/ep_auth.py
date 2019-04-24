"""
File::ep_auth.py
Author::Kevin.P.Barnett
Date::Feb.25.2019
"""

from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash

from poll_system.utilities.util_token import generate_token_with_claims, validate_token
from poll_system.utilities.util_database import get_db

import json

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/new', methods=['POST'])
def post_new_user():
    slack_id = request.form['user_id']
    passed_data = request.form['text'].split(' ')

    print(request.form)

    if len(passed_data) != 2:
        print('Bad Arguments')
        return json.dumps({'msg': 'incorrect number of arguments'}), 400

    username = passed_data[0]
    password = passed_data[1]

    if slack_id is None:
        print('Not Great Arguments')
        return json.dumps({'msg': 'either username or password is not entered'}), 400

    get_db().execute('INSERT INTO users VALUES (?, ?, ?, ?)', (slack_id, username, generate_password_hash(password), False))
    print(get_db().commit())

    return json.dumps({'msg': 'Account Created'}), 200


@bp.route('/login', methods=['POST'])
def post_login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    return_data = {'msg': 'either username or password is incorrect', 'token': ''}

    if username is None or password is None:
        return json.dumps(return_data), 400

    userRow = get_db().execute('SELECT * FROM users WHERE username=?', (username,)).fetchone()
    if userRow is None:
        return json.dumps(return_data), 400

    if check_password_hash(userRow['password'], password):
        return_data = {
            'msg': 'Successfully logged in',
            'token': generate_token_with_claims({
                'user_id': userRow['slack_id'],
                'role': 'admin' if userRow['is_admin'] else 'member'
            }).decode()
        }
        return json.dumps(return_data), 200

    return json.dumps(return_data), 400


@bp.route('/logout', methods=['POST'])
@validate_token
def post_logout():
    pass