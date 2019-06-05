"""
File::__init__.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_json('config.json')

    from poll_system.endpoints import ep_auth
    from poll_system.endpoints import ep_poll
    from poll_system.utilities import util_database

    util_database.init_app(app)

    app.register_blueprint(ep_poll.bp)
    app.register_blueprint(ep_auth.bp)

    return app


poll_system = create_app()
