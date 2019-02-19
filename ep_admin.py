"""
File::ep_admin.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/polls', method='GET')
def get_polls():
    pass


@bp.route('/polls', method='POST')
def post_polls():
    pass


@bp.route('/polls', method='PUT')
def put_polls():
    pass


@bp.route('/polls', method='DELETE')
def del_polls():
    pass


@bp.route('/superAdmin', method='PUT')
def put_super_admin():
    pass
