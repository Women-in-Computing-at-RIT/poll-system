"""
File::__init__.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

import os
from .config import ProductionConfig, DevelopmentConfig
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('POLL_PROD') is not None:
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    from . import db, ep_app, ep_auth, ep_slack, ep_admin
    db.init_app(app)

    app.register_blueprint(ep_app.bp)
    app.register_blueprint(ep_auth.bp)
    app.register_blueprint(ep_slack.bp)
    app.register_blueprint(ep_admin.bp)

    return app
