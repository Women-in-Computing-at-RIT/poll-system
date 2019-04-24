"""
File::util_database.py.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from .util_config import Config

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    init_db()


def init_db():
    print('connecting to database')
    db = sqlite3.connect(
            Config.DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    g.db.row_factory = sqlite3.Row

    with open(Config.DATABASE+'schema.sql') as f:
        db.executescript(f.read())


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
