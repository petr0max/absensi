from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Permission
from ..hadir.models import Absen, Sick, Permit
from ..profil.models import Profile
from ..decorators import admin_required, permission_required
from sqlalchemy import cast, func, Time
from sqlalchemy.orm import outerjoin
import datetime


@main.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
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

    checkins = cast(Absen.jam_datang, Time)
    checkouts = cast(Absen.jam_pulang, Time)
    absen_now = db.session.query(Absen, User, Profile, checkins, checkouts).select_from(Absen).outerjoin(
        User, Profile).filter(
        Absen.dates==datetime.date.today()).all()

    s_now = db.select([func.count(Sick.member_id)]).where(
        Sick.input_date==datetime.date.today())  # Counting sick dates
    count_sick_now = db.session.execute(s_now)

    sick_now = db.session.query(Sick, User, Profile).select_from(Sick).outerjoin(
        User, Profile).filter(
        Sick.input_date==datetime.date.today()).order_by(Sick.input_date.desc())

    p_now = db.select([func.count(Permit.member_id)]).where(
        Permit.disetujui==False)  # Counting Permit Not Yet
    count_permit_now = db.session.execute(p_now)

    permit_false = db.session.query(Permit, User, Profile).select_from(Permit).outerjoin(
        User, Profile).filter(
        Permit.disetujui==False).order_by(Permit.start_date.desc())

    return render_template('index.html', not_absen=not_absen,
                           member=member, count_absen=count_absen,
                           absen_now=absen_now, count_sick_now=count_sick_now,
                           sick_now=sick_now, count_permit_now=count_permit_now,
                           permit_false=permit_false)

@main.route('/reports')
@login_required
def reports():
    query_izin = db.session.query(Permit, User, Profile).select_from(Permit).outerjoin(
        User, Profile).order_by(Permit.start_date.desc())
    
    query_sick = db.session.query(Sick, User, Profile).select_from(Sick).outerjoin(
        User, Profile).order_by(Sick.input_date.desc())
    

    checkins = cast(Absen.jam_datang, Time)
    checkouts = cast(Absen.jam_pulang, Time)
    query_absen = db.session.query(Absen, User, Profile, checkins, checkouts).select_from(Absen).outerjoin(
        User, Profile).order_by(Absen.dates.desc())
    return render_template('report/index.html', query_izin=query_izin,
                           query_sick=query_sick, query_absen=query_absen)
