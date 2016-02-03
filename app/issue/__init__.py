from flask import Blueprint

issue = Blueprint('issue', __name__)

from . import views
