from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')
