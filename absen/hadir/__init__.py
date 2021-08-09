from flask import Blueprint


hadir = Blueprint('hadir', __name__)


from . import views, models
