from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from datetime import datetime
from . import hadir
from .. import db
from .models import CheckIn, CheckOut, Permit, Sick
from .forms import (PermitForm, CheckInForm, CheckOutForm, SickForm)


@hadir.route('/')
@login_required
def index():
    return render_template('hadir/hadir.html')


@hadir.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    form = CheckInForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checknow = CheckIn.query.filter_by(member_id=g.user).first()
        if checknow is None:
            checkin = CheckIn(tgl=form.tgl.data,
                              jam_datang=form.jam_datang.data,
                              member_id=g.user)
            db.session.add(checkin)
            db.session.commit()
            flash('Semangat ...!')
            return redirect(url_for('.index'))
        flash('Data sudah ada')
    checkins = CheckIn.query.order_by(CheckIn.jam_datang.desc()).all()
    return render_template('hadir/masuk.html', form=form, checkins=checkins)


@hadir.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckOutForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checknow = CheckOut.query.filter_by(member_id=g.user).first()
        if checknow is None:
            checkout = CheckOut(tgl=form.tgl.data,
                                jam_pulang=form.jam_pulang.data,
                                keterangan=form.keterangan.data,
                                member_id=g.user
                                )
            db.session.add(checkout)
            db.session.commit()
            flash('Selamat Beristirahat...')
            return redirect(url_for('.index'))
        flash('Data sudah ada')
    checkouts = CheckOut.query.order_by(CheckOut.jam_pulang.desc()).all()
    return render_template('hadir/pulang.html', form=form, checkouts=checkouts)


@hadir.route('/permit', methods=['GET', 'POST'])
@login_required
def permit():
    form = PermitForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checknow = Permit.query.filter_by(member_id=g.user).first()
        if checknow is None:
            permit = Permit(long_date=form.long_date.data,
                            start_date=form.start_date.data,
                            keterangan=form.keterangan.data,
                            member_id=g.user)
            db.session.add(permit)
            db.session.commit()
            flash('Kita coba review yah...')
            return redirect(url_for('.index'))
        flash('Data sudah ada')
    permits = Permit.query.order_by(Permit.start_date.desc()).all()
    return render_template('hadir/izin.html', form=form, permits=permits)


@hadir.route('/sick', methods=['GET', 'POST'])
@login_required
def sick():
    form = SickForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checknow = Sick.query.filter_by(member_id=g.user).first()
        if checknow is None:
            sick = Sick(tgl=form.tgl.data,
                        long_date=form.long_date.data,
                        keterangan=form.keterangan.data,
                        member_id=g.user)
            db.session.add(sick)
            db.session.commit()
            flash('Semoga Lekas Sembuh...')
            return redirect(url_for('.index'))
        flash('Data sudah ada')
    sicks= Sick.query.order_by(Sick.tgl.desc()).all()
    return render_template('hadir/sakit.html', form=form, sicks=sicks)
