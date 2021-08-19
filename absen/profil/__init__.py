from flask import Blueprint


profil = Blueprint('profil', __name__)


from . import models, views
