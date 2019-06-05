"""
File::ep_poll.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Blueprint, request, g
from poll_system.utilities.util_token import validate_token
from poll_system.objects.obj_poll import Poll, Option

from uuid import uuid4
from time import time
import json

bp = Blueprint('poll', __name__, url_prefix='/poll')


@bp.route('/list', methods=['GET'])
@validate_token
def get_polls(token):
    poll_types = request.args.get('type', default='current', type=str).split(',')

    return_polls = {}

    for type in poll_types:
        if type is 'user':
            return_polls[type] = Poll.query.filter_by(type='user', author=token.get('user_id')).all()
        else:
            return_polls[type] = Poll.query.filter_by(type=type).all()

    return json.dumps(return_polls), 200


@bp.route('/new', methods=['PUT'])
@validate_token
def put_new_poll(token):
    poll = Poll.getFromDict(json.loads(request.data))
    poll.timestamp = time()
    for option in request.get_json()['options']:
        tmp_option = Option()
        tmp_option.option_id = str(uuid4())
        tmp_option.poll_id = poll.id
        tmp_option.option_text = option
        poll.options += tmp_option

    g.db.session.add(poll)
    g.db.session.commit()

    return json.dumps({
        'msg': 'poll created successfully'
    }), 200


@bp.route('/delete', methods=['DELETE'])
def delete_poll(token):
    if token.get('role') is 'admin':
        poll_id = request.data.get('poll_id')


@bp.route('/asdfasdf', methods=['POST'])
def put_polls():
    pass
