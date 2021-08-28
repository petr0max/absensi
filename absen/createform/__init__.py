from flask import Blueprint


createform = Blueprint('createform', __name__)


from . import models
