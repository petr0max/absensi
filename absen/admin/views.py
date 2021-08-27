from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from sqlalchemy.sql import func
from ..hadir.models import Absen
from . import admins
import datetime
from ..decorators import admin_required 
from .. import db


@admins.route('/')
@login_required
def index():
    cmt = db.select([func.count(Absen.member_id)]).where(
        Absen.dates==datetime.date.today())
    count_absen = db.session.execute(cmt)
    return render_template('admin/index.html', count_absen=count_absen)
