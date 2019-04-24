"""
File::ep_poll.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Blueprint, request
from utilities.util_token import validate_token
from objects.obj_poll import Poll
from utilities.util_database import get_db

from uuid import uuid4
from time import time
import json

bp = Blueprint('poll', __name__, url_prefix='/poll')


@bp.route('/list', methods=['GET'])
@validate_token
def get_polls(token):
    poll_types = request.args.get('type', default='current', type=str).split(',')
    db = get_db()

    return_polls = {}

    for type in poll_types:
        if type is 'user':
            return_polls[type] = db.execute('SELECT * FROM polls WHERE type = ? AND author = ?', (type, token.get('user_id')))
        else:
            return_polls[type] = db.execute('SELECT * FROM polls WHERE type = ?', (type,)).fetchall()

    return json.dumps(return_polls), 200


@bp.route('/new', methods=['PUT'])
@validate_token
def put_new_poll(token):
    try:
        poll = json.loads(request.data, object_hook=Poll)
        db = get_db()

        db.execute('INSERT INTO polls VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
                   (poll.id, token.get('user_id'), poll.name, poll.description, poll.can_add, poll.multi_select, int(time()), 'pending'))

        for option in poll.options:
            db.execute('INSERT INTO options VALUES(?, ?, ?)',
                       (str(uuid4()), poll.id, option))

        db.commit()

    except KeyError as e:
        missing_keys = str([key for key in e.args])
        print('Missing required key(s): '+missing_keys)
        return json.dumps({
            'msg': 'missing required key(s): '+missing_keys
        }), 400

    return json.dumps({
        'msg': 'poll created successfully'
    }), 200


@bp.route('/delete', methods=['DELETE'])
def delete_poll(token):
    if token.get('role') is 'admin':
        poll_id = request.data.get('poll_id')
        db.execute('DELETE FROM polls ')


@bp.route('/asdfasdf', methods=['POST'])
def put_polls():
    pass
