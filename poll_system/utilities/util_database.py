"""
File::util_database.py.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""
from flask import g
from flask_sqlalchemy import SQLAlchemy


def init_app(app):
    g.db = SQLAlchemy(app)
    g.db.create_all()
