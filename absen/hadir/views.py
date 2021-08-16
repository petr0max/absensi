from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import hadir
from .. import db
from .forms import (PermitForm, CheckInForm, CheckOutForm)


@hadir.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('hadir/hadir.html')


@hadir.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    return render_template('hadir/masuk.html')


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
