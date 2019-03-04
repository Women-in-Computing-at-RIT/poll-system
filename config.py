"""
File::config.py
Author::Kevin.P.Barnett
Date::Mar.04.2019
"""


class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
