from flask import (render_template, redirect, request, url_for, flash, g,
                   session)
from flask_login import login_required, current_user
from datetime import datetime
from . import hadir
from .. import db
from .models import CheckIn, CheckOut, Permit, Sick
from .forms import (PermitForm, CheckInForm, CheckOutForm, SickForm)


@hadir.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('hadir/hadir.html')

@hadir.route('/report/<string:username>', methods=['GET', 'POST'])
@login_required
def report():
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('hadir/hadir.html', user=user)

@hadir.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    form = CheckInForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        checkin = CheckIn(tgl=form.tgl.data,
                          jam_datang=form.jam_datang.data,
                          checkin_id=g.user)
        db.session.add(checkin)
        db.session.commit()
        flash('Selamat Berkreativas!')
        return redirect(url_for('.index'))
    checkins = CheckIn.query.order_by(CheckIn.jam_datang.desc()).all()
    return render_template('hadir/masuk.html', form=form, checkins=checkins)


@hadir.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template('hadir/pulang.html')


@hadir.route('/permit', methods=['GET', 'POST'])
@login_required
def permit():
    return render_template('hadir/izin.html')

@hadir.route('/sick', methods=['GET', 'POST'])
@login_required
def sick():
    return render_template('hadir/sakit.html')
