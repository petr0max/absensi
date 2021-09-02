from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from . import hadir
from .. import db
from ..models import User
from ..profil.models import Profile
from .models import Permit, Absen, Sick
from .forms import (PermitForm, CheckInForm, CheckOutForm, SickForm,
                    PermitConfirmForm)
from sqlalchemy import cast, Time
from ..decorators import admin_required
import datetime


@hadir.route('/')
@login_required
def index():
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()

    checkins = cast(Absen.jam_datang, Time)
    checkouts = cast(Absen.jam_pulang, Time)
    query_absen = db.session.query(Absen, User, Profile, checkins, checkouts).select_from(
        Absen).outerjoin(User, Profile).filter(Absen.member_id==g.user).order_by(Absen.dates.desc())

    query_izin = db.session.query(Permit, User, Profile).select_from(
        Permit).outerjoin(User, Profile).filter(Permit.member_id==g.user).order_by(Permit.start_date.desc())

    query_sick = db.session.query(Sick, User, Profile).select_from(
        Sick).outerjoin(User, Profile).filter(Sick.member_id==g.user).order_by(Sick.input_date.desc())
    
    return render_template('hadir/hadir.html', query_absen=query_absen,
                           profil=profil, query_izin=query_izin,
                           query_sick=query_sick)


@hadir.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    form = CheckInForm()
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    checkin = Absen.query.filter(Absen.dates==form.dates.data, Absen.member_id==g.user).first()
    if request.method == 'POST':
        if checkin is None:
            jam_input = form.jam_input.data
            clock_input = datetime.datetime.strptime(str(jam_input), '%H:%M:%S')
            date_input = form.dates.data
            tgl_input = datetime.datetime.strptime(str(date_input), "%Y-%m-%d")
            
            checkin = Absen()
            checkin.dates=date_input
            checkin.jam_datang=datetime.datetime.combine(datetime.date(
                tgl_input.year, tgl_input.month, tgl_input.day), datetime.time(clock_input.hour, clock_input.minute))
            checkin.member_id=g.user
            db.session.add(checkin)
            db.session.commit()
            flash('Semangat ...!')
            return redirect(url_for('.index'))
            return render_template('hadir/masuk.html', form=form,
                                   checkin=checkin, profil=profil)
        
        else:
            flash('Upss... sudah checkin kak!')
            return redirect(url_for('hadir.checkin'))
            return render_template('hadir/masuk.html', form=form,
                                   checkin=checkin, profil=profil)
    
    else:
        return render_template('hadir/masuk.html', form=form, profil=profil)


@hadir.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckOutForm()
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    checkouts = Absen.query.filter(Absen.dates==form.dates.data, Absen.member_id==g.user).first()
    
    if request.method == 'POST':
        if checkouts:
            jam_input = form.jam_pulang.data
            clock_input = datetime.datetime.strptime(str(jam_input), '%H:%M:%S')
            date_input = form.dates.data
            tgl_input = datetime.datetime.strptime(str(date_input), "%Y-%m-%d")
            
            checkouts.jam_pulang=datetime.datetime.combine(datetime.date(
                tgl_input.year, tgl_input.month, tgl_input.day), datetime.time(clock_input.hour, clock_input.minute))
            checkouts.keterangan = form.keterangan.data
            db.session.commit()
            flash('Selamat Beristirahat...')
            return redirect(url_for('.index'))
            return render_template('hadir/pulang.html', form=form,
                                   checkouts=checkouts, profil=profil)
        else:
            flash('Anda belum checkin tanggal tersebut...')
            return redirect(url_for('.index'))
    
    else:
        return render_template('hadir/pulang.html', form=form, profil=profil)


@hadir.route('/sick', methods=['GET', 'POST'])
@login_required
def sick():
    form = SickForm()
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    sakit = Sick.query.filter(Sick.input_date==form.input_date.data,
                              Sick.member_id==g.user).first()
    if request.method=='POST':
        if sakit is None:
            sakit = Sick()
            sakit.input_date=form.input_date.data
            sakit.diagnosa=form.diagnosa.data
            sakit.long_date=form.long_date.data
            sakit.member_id=g.user
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
            sakit.input_date=form.input_date.data
            sakit.diagnosa=form.diagnosa.data
            sakit.long_date=form.long_date.data
            try:
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
    profiles = Profile.query.filter(Profile.member_id==g.user).first()
    permits = Permit.query.filter(Permit.start_date==form.start_date.data, Permit.member_id==g.user).first()
    if request.method=='POST':
        if permits is None:
            permits = Permit()
            permits.long_date=form.long_date.data
            permits.start_date=form.start_date.data
            permits.keterangan=form.keterangan.data
            permits.member_id=g.user
            try:
                db.session.add(permits)
                db.session.commit()
                flash('Kita coba review yah...')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, profiles=profiles)
            except:
                flash('Error! Looks like there was a problem. Try again...')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, profiles=profiles)
        else:
            permits.long_date=form.long_date.data
            permits.start_date=form.start_date.data
            permits.keterangan=form.keterangan.data
            try:
                db.session.commit()
                flash('Update berhasil...')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, profiles=profiles)
            except:
                flash('Error! Looks like there was a problem. Try again...')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, profiles=profiles)

        flash('Permintaan izin sudah ada.')
    else:
        return render_template('hadir/input_izin.html', form=form,
                               profiles=profiles)

@hadir.route('/izin/edit/<int:id>')
@login_required
@admin_required
def confirmed(id):
    form = PermitConfirmForm()
    users = User.query.filter(User.id==id).first()
    profiles = Profile.query.filter(Profile.member_id==users.id).first()
    permits = Permit.query.filter(Permit.id==id).first()
    if request.method=='POST':
        if permits:
            permits.agree = form.checkbox.data
            try:
                db.session.commit()
                flash('Data telah terkonfirmasi')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, users=users,
                                       profiles=profiles)
            except:
                flash('Data tidak disetujui')
                return redirect(url_for('.index'))
                return render_template('hadir/input_izin.html', form=form,
                                       permits=permits, users=users,
                                       profiles=profiles)
    else:
        return render_template('hadir/input_izin.html', form=form,
                               profiles=profiles)
