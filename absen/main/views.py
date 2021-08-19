from datetime import datetime
from flask import (render_template, session, redirect, url_for, flash, abort,
                   request)
from flask_login import login_required, current_user
from . import main
from .. import db
from .forms import EditProfileForm
from ..models import User, Permission
from ..decorators import admin_required, permission_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


@main.route('/admin/<username>')
@login_required
@admin_required
def for_admin_only(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('index.html', user=user)


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "For comment moderators!"


@main.route('/profil/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@main.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        current_user.study = form.study.data
        current_user.jurusan = form.jurusan.data
        current_user.gelar = form.gelar.data
        current_user.address_before = form.address_before.data
        current_user.address_now = form.address_now.data
        current_user.blood = form.blood.data
        current_user.religion = form.religion.data
        current_user.warga_negara = form.warga_negara.data
        current_user.nik = form.nik.data
        current_user.npwp = form.npwp.data
        current_user.no_hp = form.no_hp.data
        current_user.zone = form.zone.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    form.study.data = current_user.study
    form.jurusan.data = current_user.jurusan
    form.gelar.data = current_user.gelar
    form.address_before.data = current_user.address_before
    form.address_now.data = current_user.address_now
    form.blood.data = current_user.blood
    form.religion.data = current_user.religion
    form.warga_negara.data = current_user.warga_negara
    form.nik.data = current_user.nik
    form.npwp.data = current_user.npwp
    form.no_hp.data = current_user.no_hp
    form.zone.data = current_user.zone
    return render_template('account/edit_profile.html', form=form)
