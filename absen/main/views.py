from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Permission
from ..hadir.models import Absen
from ..decorators import admin_required, permission_required
from sqlalchemy.sql import func
import datetime


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    mem_id = db.session.query(func.count(User.id)).all()
    for x in mem_id:
        for y in x:
            ntabs = db.select([y-func.count(Absen.member_id)]).where(Absen.dates==datetime.date.today())
            not_absen = db.session.execute(ntabs)
    cmt = db.select([func.count(Absen.member_id)]).where(
        Absen.dates==datetime.date.today())
    count_absen = db.session.execute(cmt)
    mtid = db.select([func.count(User.id)])
    member = db.session.execute(mtid)
    return render_template('index.html', not_absen=not_absen,
                           member=member, count_absen=count_absen)
