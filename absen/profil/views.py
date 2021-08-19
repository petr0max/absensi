from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import profil
from .. import db
from .models import Profile
from .forms import EditProfileForm
from ..models import User

@profil.route('/profil/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    g.user = current_user.get_id()
    profil = Profile.query.filter_by(user_id=g.user).first()
    return render_template('user.html', user=user, profil=profil)


@profil.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    form = EditProfileForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        profil_check = Profile.query.filter_by(user_id=g.user).first()
        if profil_check is None:
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
            current_user.user_id = g.user
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
