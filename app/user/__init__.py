__author__ = 'corentin'
from flask import Blueprint

user = Blueprint('user', __name__, template_folder='templates')
import views


def register_blueprint(app):
    app.register_blueprint(user, url_prefix='/users')
