from datetime import datetime
from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import profile
from .. import db
from .models import Profile
from ..models import User
from .forms import EditProfileForm


@profile.route('/<username>')
@login_required
def index(username):
    user = User.query.filter_by(username=username).first_or_404()
    g.user = current_user.get_id()
    profil = Profile.query.filter_by(member_id=g.user).first()
    return render_template('user.html', user=user, profil=profil)


@profile.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        g.user = current_user.get_id()
        profiles = Profile.query.filter(Profile.member_id==g.user).first()
        if profiles is None:
            profil = Profile(
                realname = form.realname.data,
                location = form.location.data,
                about_me = form.about_me.data,
                study = form.study.data,
                jurusan = form.jurusan.data,
                gelar = form.gelar.data,
                address_before = form.address_before.data,
                address_now = form.address_now.data,
                blood = form.blood.data,
                religion = form.religion.data,
                warga_negara = form.warga_negara.data,
                nik = form.nik.data,
                npwp = form.npwp.data,
                no_hp = form.no_hp.data,
                zone = form.zone.data,
                member_id = g.user)
            db.session.add(profil)
            db.session.commit()
            flash('Update Profil Berhasil!')
            return redirect(url_for('profile.index', username=current_user.username))
        else:
            profiles.realname = form.realname.data
            profiles.location = form.location.data
            profiles.about_me = form.about_me.data
            profiles.study = form.study.data
            profiles.jurusan = form.jurusan.data
            profiles.gelar = form.gelar.data
            profiles.address_before = form.address_before.data
            profiles.address_now = form.address_now.data
            profiles.blood = form.blood.data
            profiles.religion = form.religion.data
            profiles.warga_negara = form.warga_negara.data
            profiles.nik = form.nik.data
            profiles.npwp = form.npwp.data
            profiles.no_hp = form.no_hp.data
            profiles.zone = form.zone.data
            db.session.commit()
            flash('Update Profil Berhasil!')
            return redirect(url_for('profile.index', username=current_user.username))
    return render_template('account/edit_profile.html', form=form)
