from .. import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_lengkap = db.Column(db.String(64), index=True)
    tempat_lahir = db.Column(db.String(64), index=True)
    tanggal_lahir = db.Column(db.Date(), default=datetime.date.today())
    lokasi = db.Column(db.String(64), index=True)
    tentang_saya = db.Column(db.Text())
    divisi = db.Column(db.String(64), index=True)
    jabatan = db.Column(db.String(64), index=True)
    status_pegawai = db.Column(db.String(64), index=True)
    pendidikan_terakhir = db.Column(db.String(64), index=True)
    gelar_pendidikan = db.Column(db.String(64), index=True)
    nama_almamater = db.Column(db.String(64), index=True)
    jurusan = db.Column(db.String(64), index=True)
    alamat_asal = db.Column(db.String(64), index=True)
    alamat_domisili = db.Column(db.String(64), index=True)
    golongan_darah = db.Column(db.String(64), index=True)
    jenis_kelamin = db.Column(db.String(64), index=True)
    status_pernikahan = db.Column(db.String(64), index=True)
    agama = db.Column(db.String(64), index=True)
    warga_negara = db.Column(db.String(64), index=True)
    nik = db.Column(db.Integer, index=True)
    npwp = db.Column(db.Integer, index=True)
    no_bpjs_ketenagakerjaan = db.Column(db.Integer, index=True)
    no_bpjs_kesehatan = db.Column(db.Integer, index=True)
    no_hp = db.Column(db.Integer, index=True)
    zona_waktu = db.Column(db.String(64), index=True)

    # Create Bank account detail
    nama_bank = db.Column(db.String(64), index=True)
    nama_rekening = db.Column(db.String(64), index=True)
    no_rekening = db.Column(db.Integer, index=True)

    # Create for parent profile user
    nama_wali = db.Column(db.String(64), index=True)
    hubungan_wali = db.Column(db.String(64), index=True)
    alamat_wali = db.Column(db.String(64), index=True)
    no_kontak_wali = db.Column(db.Integer, index=True)

    member_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    childs = db.relationship('Child', backref='profile', lazy='dynamic')
    parents = db.relationship('Parent', backref='profile', lazy='dynamic')

    def __repr__(self):
        return f"{self.nama_lengkap.title()}"


class Child(db.Model):
    __tablename__ = 'childs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    nama_anak = db.Column(db.String(64), index=True)


class Parent(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    nama_wali = db.Column(db.String(64), index=True)
    hubungan_wali = db.Column(db.String(64), index=True)
    alamat_wali = db.Column(db.String(64), index=True)
