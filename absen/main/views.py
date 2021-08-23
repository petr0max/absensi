from datetime import datetime
from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Permission
from ..profil.models import Profile
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')
