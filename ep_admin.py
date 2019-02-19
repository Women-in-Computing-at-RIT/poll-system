"""
File::ep_admin.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/polls', methods=['GET'])
def get_polls():
    pass


@bp.route('/polls', methods=['POST'])
def post_polls():
    pass


@bp.route('/polls', methods=['PUT'])
def put_polls():
    pass


@bp.route('/polls', methods=['DELETE'])
def del_polls():
    pass


@bp.route('/superAdmin', methods=['PUT'])
def put_super_admin():
    pass
