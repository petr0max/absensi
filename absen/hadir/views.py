from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import hadir
from .. import db
from .forms import (PermitForm, CheckInForm, CheckOutForm)


@hadir.route('/hadir', methods=['GET', 'POST'])
