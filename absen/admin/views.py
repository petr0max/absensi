from flask import request, url_for, flash, redirect
from flask_login import login_required, current_user
from ..decorators import admin_required, permission_required
from . import adm


@adm.before_app_request
def before_request():
    if current_user.is_authenticated:
        if current_user.is_administrator \
                and request.endpoint \
                and request.blueprint != 'adm' \
                and request.endpoint != 'static':
            return redirect(url_for('main.index'))
