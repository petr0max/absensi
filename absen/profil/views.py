from datetime import datetime
from flask import (render_template, session, redirect, url_for, flash, abort,
                   request, g)
from flask_login import login_required, current_user
from . import profil
from .. import db
from .models import Profile, Child
from ..models import User
from .forms import EditProfileForm


@profil.route('/<username>', methods=['GET', 'POST'])
def index(username):
    user = User.query.filter_by(username=username).first_or_404()
    g.user = current_user.get_id()
    profil = Profile.query.filter(Profile.member_id==g.user).first()
    return render_template('user.html', user=user, profil=profil)


@profil.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method=='POST' and form.validate_on_submit():
        g.user = current_user.get_id()
        profiles = Profile.query.filter(Profile.member_id==g.user).first()
        # childs = Child.query.filter(Child.member_id==g.user).first()
        if profiles is None:
            profil = Profile(
                nama_lengkap = request.form['nama_lengkap'],
                tempat_lahir = form.tempat_lahir.data,
                tanggal_lahir = form.tanggal_lahir.data,
                tentang_saya = form.tentang_saya.data,
                divisi = str(form.divisi.data),
                jabatan = str(form.jabatan.data),
                lokasi_kantor = str(form.lokasi_kantor.data),
                status_pegawai = str(form.status_pegawai.data),
                pendidikan_terakhir = str(form.pendidikan_terakhir.data),
                gelar_pendidikan = form.gelar_pendidikan.data,
                nama_almamater = form.nama_almamater.data,
                jurusan = form.jurusan.data,
                alamat_asal = form.alamat_asal.data,
                alamat_domisili = form.alamat_domisili.data,
                golongan_darah = str(form.golongan_darah.data),
                jenis_kelamin = str(form.jenis_kelamin.data),
                status_pernikahan = str(form.status_pernikahan.data),
                nama_pasangan = form.nama_pasangan.data,
                agama = str(form.agama.data),
                warga_negara = str(form.warga_negara.data),
                nik = form.nik.data,
                npwp = form.npwp.data,
                no_bpjs_ketenagakerjaan = form.no_bpjs_ketenagakerjaan.data,
                no_bpjs_kesehatan = form.no_bpjs_kesehatan.data,
                no_hp = form.no_hp.data,
                zona_waktu = str(form.zona_waktu.data),
                nama_bank = str(form.nama_bank.data),
                nama_rekening = form.nama_rekening.data,
                no_rekening = form.no_rekening.data,
                nama_wali = form.nama_wali.data,
                hubungan_wali = str(form.hubungan_wali.data),
                alamat_wali = form.alamat_wali.data,
                no_kontak_wali = form.no_kontak_wali.data,
                member_id = g.user)
            db.session.add(profil)
            db.session.commit()
            flash('Update Profil Berhasil!')
            return redirect(url_for('profil.index', username=current_user.username))
        else:
            profiles.nama_lengkap = request.form['nama_lengkap'] 
            profiles.tempat_lahir = form.tempat_lahir.data
            profiles.tanggal_lahir = form.tanggal_lahir.data
            profiles.tentang_saya = form.tentang_saya.data
            profiles.divisi = str(form.divisi.data)
            profiles.jabatan = str(form.jabatan.data)
            profiles.lokasi_kantor = str(form.lokasi_kantor.data)
            profiles.status_pegawai = str(form.status_pegawai.data)
            profiles.pendidikan_terakhir = str(form.pendidikan_terakhir.data)
            profiles.gelar_pendidikan = form.gelar_pendidikan.data
            profiles.nama_almamater = form.nama_almamater.data
            profiles.jurusan = form.jurusan.data
            profiles.alamat_asal = form.alamat_asal.data
            profiles.alamat_domisili = form.alamat_domisili.data
            profiles.golongan_darah = str(form.golongan_darah.data)
            profiles.jenis_kelamin = str(form.jenis_kelamin.data)
            profiles.status_pernikahan = str(form.status_pernikahan.data)
            profiles.nama_pasangan = form.nama_pasangan.data
            profiles.agama = str(form.agama.data)
            profiles.warga_negara = str(form.warga_negara.data)
            profiles.nik = form.nik.data
            profiles.npwp = form.npwp.data
            profiles.no_bpjs_ketenagakerjaan = form.no_bpjs_ketenagakerjaan.data
            profiles.no_bpjs_kesehatan = form.no_bpjs_kesehatan.data
            profiles.no_hp = form.no_hp.data
            profiles.zona_waktu = str(form.zona_waktu.data)
            profiles.nama_bank = str(form.nama_bank.data)
            profiles.nama_rekening = form.nama_rekening.data
            profiles.no_rekening = form.no_rekening.data
            profiles.nama_wali = form.nama_wali.data
            profiles.hubungan_wali = str(form.hubungan_wali.data)
            profiles.alamat_wali = form.alamat_wali.data
            profiles.no_kontak_wali = form.no_kontak_wali.data
            db.session.commit()
            flash('Update Profil Berhasil!')
            return redirect(url_for('profil.index', username=current_user.username))
        flash('Uppss... bermasalah...')
    return render_template('account/edit_profile.html', form=form)
