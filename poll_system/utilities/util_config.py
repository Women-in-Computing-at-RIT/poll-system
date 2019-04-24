"""
File::util_config.py
Author::Kevin.P.Barnett
Date::Mar.04.2019
"""

import os


class Config(object):
    DEBUG = False
    DATABASE = '~/poll.db'
    SCHEMA_PATH = '~/poll_system/'
    SECRET_KEY = 'REPLACE'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('POLL_SECRET')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
