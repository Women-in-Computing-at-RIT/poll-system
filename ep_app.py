"""
File::ep_app.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""
import sqlite3
import logging
import json

from flask import Blueprint, request, current_app
from .db import get_db, close_db

bp = Blueprint('app', __name__, url_prefix='/app')


@bp.route('/polls', methods=['GET'])
def get_polls():
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM poll;")
        raw_data = cursor.fetchall()
        data = [list(x) for x in raw_data]
        return json.dumps({'msg': 'Successfully got all the polls', 'data': data}), 200
    except sqlite3.Error as e:
        logging.error(e)
        return json.dumps({'msg': 'Failed to get the polls'}), 404
    finally:
        close_db()


@bp.route('/polls', methods=['POST'])
def post_polls():
    author = request.json.get('author', None)
    title = request.json.get('title', None)

    if author is None or title is None:
        return json.dumps({'msg': 'Either poll_id or author or title is not entered'}), 422

    conn = get_db()
    try:
        conn.execute("INSERT INTO poll(author, title) VALUES('{}', '{}');".format(author, title))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(e)
    finally:
        close_db()
        return json.dumps({'msg': 'Successfully inserted the poll'}), 200


@bp.route('/polls', methods=['PUT'])
def put_polls():
    poll_id = request.json.get('poll_id', None)
    author = request.json.get('author', None)
    title = request.json.get('title', None)

    if poll_id is None or author is None or title is None:
        return json.dumps({'msg': 'Either poll_id or author or title is not entered'}), 404
    conn = get_db()
    try:
        conn.execute("UPDATE poll SET author='{}', title='{}' WHERE poll_id='{}';".format(author, title, poll_id))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(e)
        return json.dumps({'msg': 'Failed to update the poll'}), 422
    finally:
        close_db()
        return json.dumps({'msg': 'Successfully updated the poll'}), 200
