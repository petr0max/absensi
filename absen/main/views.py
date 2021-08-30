from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Permission
from ..hadir.models import Absen
from ..profil.models import Profile
from ..decorators import admin_required, permission_required
from sqlalchemy.sql import func
import datetime


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # mem_id is point to query member id on table User
    mem_id = db.session.query(func.count(User.id)).all()
    for x in mem_id:
        for y in x:
            ntabs = db.select([y-func.count(Absen.member_id)]).where(Absen.dates==datetime.date.today())
            not_absen = db.session.execute(ntabs)  # counting for member not available

    cmt = db.select([func.count(Absen.member_id)]).where(
        Absen.dates==datetime.date.today(), Absen.jam_datang.isnot(None))
    count_absen = db.session.execute(cmt)  # counting absen for user available now

    mtid = db.select([func.count(User.id)])
    member = db.session.execute(mtid)  # Counting member on database register

    absen_now = db.session.query(User, Absen, Profile).join(Absen, Profile).filter(
        Absen.dates==datetime.date.today()).all()
    return render_template('index.html', not_absen=not_absen,
                           member=member, count_absen=count_absen,
                           absen_now=absen_now)
