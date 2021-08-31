from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from datetime import datetime
from . import hadir
from .. import db
from ..models import User
from ..profil.models import Profile
from .models import Permit, Absen, Sick
from .forms import (PermitForm, CheckInForm, CheckOutForm, SickForm)


@hadir.route('/')
@login_required
def index():
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    query_absen = db.session.query(User, Absen).join(Absen).filter(
        Absen.member_id==g.user).order_by(Absen.dates.desc())
    query_izin = db.session.query(User, Permit).join(Permit).filter(Permit.member_id==g.user).order_by(Permit.start_date.desc())

    query_sick = db.session.query(User, Sick).join(Sick).filter(Sick.member_id==g.user).order_by(Sick.input_date.desc())
    return render_template('hadir/hadir.html', query_absen=query_absen,
                           profil=profil, query_izin=query_izin,
                           query_sick=query_sick)


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
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    return render_template('hadir/masuk.html', form=form, profil=profil)


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
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    return render_template('hadir/pulang.html', form=form, profil=profil)


@hadir.route('/sick/<int:id>', methods=['GET', 'POST'])
@login_required
def sick(id):
    form = SickForm()
    users = User.query.get_or_404(id)
    profil = Profile.query.filter(Profile.member_id==users.id).first()
    if request.method=='POST':
        sakit = Sick()
        sakit.diagnosa=form.diagnosa.data
        sakit.long_date=form.long_date.data
        sakit.member_id=users.id
        try:
            db.session.add(sakit)
            db.session.commit()
            flash('Semoga Lekas Sembuh...')
            return redirect(url_for('.index'))
            return render_template('hadir/sakit.html', form=form,
                                   sakit=sakit, profil=profil)
        except:
            flash('Error! Looks like there was a problem. Try again...')
            return redirect(url_for('.index'))
            return render_template('hadir/sakit.html', form=form,
                                   sakit=sakit, profil=profil)
    else:
        return render_template('hadir/sakit.html', form=form,
                               profil=profil)

@hadir.route('/izin', methods=['GET', 'POST'])
@login_required
def create_izin():
    form = PermitForm()
    g.user = current_user.get_id()
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
            return redirect(url_for('hadir.index'))
        flash('Permintaan izin sudah ada.')
    permits = Permit.query.order_by(Permit.start_date.desc()).all()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    return render_template('hadir/input_izin.html', form=form, permits=permits,
                           profil=profil)
