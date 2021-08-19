from datetime import datetime
from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Permission
from ..profile.models import Profile
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


@main.route('/admin/<username>')
@login_required
@admin_required
def for_admin_only(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('index.html', user=user)


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "For comment moderators!"
