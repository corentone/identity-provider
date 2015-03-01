from flask import Flask

import user



# See flask-bones for more granular
def create_app():
    """

    :rtype : Flask
    """
    app = Flask(__name__)
    register_blueprints(app)

    @app.route('/')
    def main():
        return 'Hello World'

    return app


def register_blueprints(app):
    user.register_blueprint(app)


