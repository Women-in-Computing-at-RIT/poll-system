"""
File::config.py
Author::Kevin.P.Barnett
Date::Mar.04.2019
"""

import os


class Config(object):
    DEBUG = False
    DATABASE = 'd:\\poll.db'
    SCHEMA_PATH = 'd:\\Pycharm_Project\\poll-system\\'
    SECRET_KEY = 'REPLACE'


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('POLL_SECRET')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
