"""
File::ep_app.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Blueprint

bp = Blueprint('app', __name__, url_prefix='/app')


@bp.route('/polls', methods=['GET'])
def get_polls():
    return 'Hello World!'


@bp.route('/polls', methods=['POST'])
def post_polls():
    pass


@bp.route('/polls', methods=['PUT'])
def put_polls():
    pass
