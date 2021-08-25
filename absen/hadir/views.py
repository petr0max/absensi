from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from datetime import datetime
from . import hadir
from .. import db
from ..models import User
from .models import Permit, Absen
from .forms import (PermitForm, CheckInForm, CheckOutForm, SickForm)


@hadir.route('/')
@login_required
def index():
    g.user = current_user.get_id()
    query_absen = db.session.query(User, Absen).join(Absen).order_by(Absen.dates.desc())
    return render_template('hadir/hadir.html', query_absen=query_absen)


@hadir.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    form = CheckInForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checkdates = Absen.query.filter(Absen.dates==form.dates.data, Absen.member_id==g.user).first()
        if checkdates is None:
            checkin = Absen(dates=form.dates.data,
                            jam_datang=form.jam_datang.data,
                            member_id=g.user)
            db.session.add(checkin)
            db.session.commit()
            flash('Semangat ...!')
            return redirect(url_for('.index'))
        flash('Upss.. data sudah ada')
    return render_template('hadir/masuk.html', form=form)


@hadir.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckOutForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checkdates = Absen.query.filter(Absen.dates==form.dates.data, Absen.member_id==g.user).first()
        if checkdates:
            checkdates.jam_pulang = form.jam_pulang.data
            checkdates.keterangan = form.keterangan.data
            db.session.commit()
            flash('Selamat Beristirahat...')
            return redirect(url_for('.index'))
        flash('Anda belum checkin tanggal tersebut...')
    return render_template('hadir/pulang.html', form=form)


@hadir.route('/sick', methods=['GET', 'POST'])
@login_required
def sick():
    form = SickForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checkdate = Absen.query.filter(Absen.dates==form.dates.data, Absen.member_id==g.user).first()
        if checkdate is None:
            sick = Absen(dates=form.dates.data,
                        keterangan=form.keterangan.data,
                        member_id=g.user)
            db.session.add(sick)
            db.session.commit()
            flash('Semoga Lekas Sembuh...')
            return redirect(url_for('.index'))
        flash('Data sudah ada')
    return render_template('hadir/sakit.html', form=form)


@hadir.route('/izin')
@login_required
def izin():
    g.user = current_user.get_id()
    query_izin = db.session.query(User, Permit).join(Permit).order_by(Permit.start_date.desc())
    return render_template('hadir/izin.html', query_izin=query_izin)


@hadir.route('/izin/create', methods=['GET', 'POST'])
@login_required
def create_izin():
    form = PermitForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        permits = Permit.query.filter_by(member_id=g.user).first()
        checkdates = Permit.query.filter(Permit.start_date==form.start_date.data, Permit.member_id==g.user).first()
        if checkdates is None:
            permit = Permit(long_date=form.long_date.data,
                            start_date=form.start_date.data,
                            keterangan=form.keterangan.data,
                            member_id=g.user)
            db.session.add(permit)
            db.session.commit()
            flash('Kita coba review yah...')
            return redirect(url_for('.index'))
        flash('Permintaan izin sudah ada.')
    permits = Permit.query.order_by(Permit.start_date.desc()).all()
    return render_template('hadir/input_izin.html', form=form, permits=permits)
