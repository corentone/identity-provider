__author__ = 'corentin'

from flask import Blueprint

oauth2 = Blueprint('oauth2', __name__, template_folder='templates')

import views