"""
File::obj_auth.py
Author::Kevin.P.Barnett
Date::Apr.26.2019
"""

from flask import g

class User(g.db.Model):
    slack_id = g.db.Column(g.db.String(9), primary_key=True)
    username = g.db.Column(g.db.String(256), nullable=False, unique=True)
    password = g.db.Column(g.db.String(512), nullable=False)
    is_admin = g.db.Column(g.db.Boolean, nullable=False)