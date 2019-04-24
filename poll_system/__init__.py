"""
File::__init__.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

import os
from poll_system.utilities.util_config import ProductionConfig, DevelopmentConfig
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('POLL_PROD') is not None:
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    from poll_system.endpoints import ep_auth
    from poll_system.endpoints import ep_poll
    from poll_system.utilities import util_database

    util_database.init_app(app)

    app.register_blueprint(ep_poll.bp)
    app.register_blueprint(ep_auth.bp)

    return app
